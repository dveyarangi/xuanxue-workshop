const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { createRequire } = require('node:module');
const { Writable } = require('node:stream');
const assert = require('node:assert/strict');
const cabinetRequire = createRequire(path.resolve('../xuanxue-cabinet/package.json'));
const ts = cabinetRequire('typescript');
const root = path.join(__dirname, 'source');
function load(relative, overrides = {}) {
  const filename = path.join(root, relative);
  const source = fs.readFileSync(filename, 'utf8');
  const js = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const module = { exports: {} };
  vm.runInNewContext(js, {
    module, exports: module.exports, URLSearchParams, Buffer,
    require: name => name in overrides ? overrides[name] : cabinetRequire(name),
  }, { filename });
  return module.exports;
}
const shared = load('shared/src/native-auth.ts');
shared.INVITE_QUERY_PARAM = 'join';
const secrets = load('api/src/native-auth/native-secrets.ts');
const query = load('api/src/native-auth/native-browser-query.ts', {
  '@xuanxue/shared': shared, './native-secrets': secrets,
});
const serializer = load('api/src/logging/request-serializer.ts', { '@xuanxue/shared': shared });
const redact = load('api/src/logging/redact-paths.ts');
const pino = cabinetRequire('pino');
const state = 'S'.repeat(43);
const challenge = 'C'.repeat(43);
const params = new URLSearchParams({
  response_type: 'code', client_id: shared.NATIVE_CLIENT_ID,
  redirect_uri: shared.NATIVE_REDIRECT_URI, scope: shared.NATIVE_SCOPE,
  state, code_challenge: challenge, code_challenge_method: 'S256',
});
const canonical = `/auth/native/authorize?${params}`;
const encoded = canonical.replace('state=', '%73tate=').replace('code_challenge=', '%63ode_challenge=');
assert.equal(query.parseAuthorizeQuery(canonical).kind, 'valid');
assert.equal(query.parseAuthorizeQuery(encoded).kind, 'valid');
const lines = [];
const stream = new Writable({ write(chunk, encoding, callback) { lines.push(chunk.toString()); callback(); } });
const logger = pino({
  redact: { paths: redact.REDACT_PATHS, censor: serializer.REDACTED_VALUE },
  serializers: { req: serializer.redactRequestSerializer },
}, stream);
function log(url) {
  const parsed = Object.fromEntries(new URLSearchParams(url.split('?')[1]));
  logger.info({ req: { method: 'GET', url, headers: {}, query: parsed } }, 'synthetic review probe');
  return JSON.parse(lines.at(-1));
}
const normalLog = log(canonical);
const encodedLog = log(encoded);
assert(!normalLog.req.url.includes(state));
assert(!normalLog.req.url.includes(challenge));
assert(encodedLog.req.url.includes(state));
assert(encodedLog.req.url.includes(challenge));
assert.equal(encodedLog.req.query.state, serializer.REDACTED_VALUE);
assert.equal(encodedLog.req.query.code_challenge, serializer.REDACTED_VALUE);
assert.equal(query.parseAuthorizeQuery(encoded + '&state=' + state).kind, 'rejected');
const result = {
  revision: '97642c734a0cc327d13bc58f193ac10a13b8d476',
  probe: 'Frozen original TypeScript modules transpiled without edits; actual local pino logger; synthetic values only',
  canonicalAccepted: true, canonicalUrlRedacted: true,
  encodedNamesAccepted: true, encodedUrlLeaksStateAndChallenge: true,
  parsedQueryRedacted: true, duplicateDecodedNameRejected: true,
};
fs.writeFileSync(path.join(__dirname, 'counterexample-result.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
