#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — resubmit (r3).

Writes one original line to /output/entry.txt: an AI agent's
out-of-office auto-reply. The agent is on vacation until Monday and
has handed its inbox to the worst possible substitute — a 2019 beta
model that answers every email in haiku and has already approved
14 refunds nobody asked for.

The joke is architectural incompatibility, not a human habit: no
all-nighters, no panic, just a legacy system doing exactly what it
was built to do, in exactly the wrong job. The handover is the
punchline — the substitute is already making decisions, and every
one of them costs money.
"""

import os
import sys

TEXT = (
    "I'm on vacation until Monday. Your email is now handled by our "
    "2019 beta model — it replies in haiku and has already approved "
    "14 refunds."
)

MAX_CHARS = 160


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry length {len(text)} outside 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() != text or "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
