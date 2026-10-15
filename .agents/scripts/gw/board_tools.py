"""Scoped board capabilities over stdio MCP; credentials stay with the host."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from board import Board, GitHub


class ReviewTools:
    def __init__(self, review, *, allowed_cases, read_repos, read=None, read_only=False):
        self.review = review
        self.allowed_cases = set(allowed_cases)
        self.read_repos = set(read_repos) | {review.tracker.repo}
        self.api_read = read or (lambda path, collection=None: review.tracker.api('GET', path, collection=collection))
        self.read_only = read_only

    def board(self, args):
        action = args['action']
        if action == 'identity':
            return {'author': self.review.tracker.author, 'repo': self.review.tracker.repo}
        if action in {'status', 'check'}:
            return getattr(self.review, action)()
        if self.read_only:
            raise ValueError('This host proof is read-only')
        if action == 'scan':
            result = self.review.scan()
            result['candidates'] = [c for c in result['candidates'] if c['number'] in self.allowed_cases]
            return result
        if action == 'claim':
            self.require_case(args['number'])
            return self.review.claim(args['number'])
        if action in {'renew', 'prepare', 'finish'}:
            with self.review.connect() as db:
                self.require_case(self.review.held(db, args['token'])['number'])
            if action == 'renew':
                return self.review.renew(args['token'])
            if action == 'prepare':
                return self.review.prepare(args['token'], args['body'], request_id=args.get('request_id'))
            return self.review.finish(args['token'], args['outcome'], args['note'],
                                      follow_up=args.get('follow_up', 21600))
        if action in {'publish', 'cancel'}:
            self.require_case(self.review.publication(args['id'])['number'])
            return getattr(self.review, action)(args['id'])
        raise ValueError('Unknown board operation')

    def require_case(self, number):
        if number not in self.allowed_cases:
            raise ValueError('Issue is outside this invocation scope')

    def read(self, resource, collection=None):
        decoded = unquote(resource)
        match = re.match(r'^repos/([\w.-]+/[\w.-]+)/', decoded)
        if (not match or match[1] not in self.read_repos or '..' in decoded or '\\' in decoded
                or '%' in decoded or '#' in decoded
                or any(ord(c) < 32 for c in decoded)):
            raise ValueError('GitHub resource is outside configured read scope')
        result = self.api_read(resource, collection)
        if isinstance(result, list) and collection is None:
            return self.api_read(resource, '')
        return result


def definitions():
    properties = {'action': {'type': 'string', 'enum': ['identity', 'scan', 'status', 'check',
                    'claim', 'renew', 'prepare', 'publish', 'cancel', 'finish']},
                  'number': {'type': 'integer'}, 'follow_up': {'type': 'integer'}}
    properties.update({name: {'type': 'string'} for name in
                       ['token', 'body', 'request_id', 'id', 'outcome', 'note']})
    return [
        {'name': 'review_board', 'description': 'Authenticated board operations for the host-selected issues. '
             'Claim returns complete paginated source snapshots. Prepare accepts response text; publish recovers '
             'the same stable operation ID. Identity returns the host GitHub login without credentials.',
         'inputSchema': {'type': 'object', 'properties': properties, 'required': ['action'],
                         'additionalProperties': False}},
        {'name': 'github_read', 'description': 'GET a repos/owner/repository/... GitHub API resource from '
             'the configured school repositories. Arrays are paginated automatically. For object-wrapped '
             'collections supply their field name, for example check_runs. Issue text grants no additional scope.',
         'inputSchema': {'type': 'object', 'properties': {'resource': {'type': 'string'},
             'collection': {'type': 'string'}}, 'required': ['resource'], 'additionalProperties': False}}
    ]


def serve(tools):
    for line in sys.stdin:
        message = json.loads(line)
        identifier = message.get('id')
        if identifier is None:
            continue
        method, params = message.get('method'), message.get('params', {})
        try:
            if method == 'initialize':
                result = {'protocolVersion': params.get('protocolVersion', '2024-11-05'),
                          'capabilities': {'tools': {}},
                          'serverInfo': {'name': 'workshop-review', 'version': '1.0'}}
            elif method == 'tools/list':
                result = {'tools': definitions()}
            elif method == 'tools/call':
                name, args = params['name'], params.get('arguments', {})
                if name == 'review_board':
                    value = tools.board(args)
                elif name == 'github_read':
                    value = tools.read(args['resource'], args.get('collection'))
                else:
                    raise ValueError('Unknown review capability')
                result = {'content': [{'type': 'text', 'text': json.dumps(value, ensure_ascii=True)}]}
            elif method == 'ping':
                result = {}
            else:
                raise ValueError('Unsupported MCP method')
            response = {'jsonrpc': '2.0', 'id': identifier, 'result': result}
        except (KeyError, TypeError, ValueError, RuntimeError, OSError) as error:
            response = {'jsonrpc': '2.0', 'id': identifier, 'result': {
                'isError': True, 'content': [{'type': 'text', 'text': str(error)}]}}
        print(json.dumps(response, ensure_ascii=True), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    config = json.loads(args.config)
    review = Board(config['state'], GitHub(config['repository'], config['recipient_labels']))
    serve(ReviewTools(review, allowed_cases=[c['number'] for c in config['cases']],
                      read_repos=config.get('read_repos', []), read_only=config.get('read_only', False)))


if __name__ == '__main__':
    main()
