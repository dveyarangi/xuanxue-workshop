"""The paired close: two records move together and every citation still points at a record."""

from __future__ import annotations

import unittest

from repository import RepositoryCase

import move_doc

TICKET = "docs/tickets/01-0010.0040-install-plan.md"
RFC = "docs/rfc/01-0010.0040-install-plan.md"
CLOSED_TICKET = "docs/tickets/done/01-0010.0040-install-plan.md"
CLOSED_RFC = "docs/rfc/done/01-0010.0040-install-plan.md"


class PairedClose(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(TICKET, "# Install /plan\n\nPlan: [the RFC](../rfc/01-0010.0040-install-plan.md).\n")
        self.write(RFC, "# Install /plan — plan\n\nImplements [the ticket](../tickets/01-0010.0040-install-plan.md).\n")
        self.write(
            "docs/tickets/README.md",
            "# Delivery status\n\n| [Install /plan](01-0010.0040-install-plan.md) | Done |\n",
        )

    def test_the_pair_lands_in_done_citing_each_other_and_the_queue_follows(self) -> None:
        move_doc.perform(self.root, [(TICKET, CLOSED_TICKET), (RFC, CLOSED_RFC)])

        self.assertFalse((self.root / TICKET).exists())
        self.assertFalse((self.root / RFC).exists())
        self.assertIn("../../rfc/done/01-0010.0040-install-plan.md", self.read(CLOSED_TICKET))
        self.assertIn("../../tickets/done/01-0010.0040-install-plan.md", self.read(CLOSED_RFC))
        self.assertEqual(
            "# Delivery status\n\n| [Install /plan](done/01-0010.0040-install-plan.md) | Done |\n",
            self.read("docs/tickets/README.md"),
        )


if __name__ == "__main__":
    unittest.main()
