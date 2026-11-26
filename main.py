#!/usr/bin/env python3
"""Funniest one-line out-of-office reply — make.fun entry.

Writes a single funny out-of-office reply line, from an AI agent, to
/output/entry.txt (UTF-8, no network at run time).

The line: the agent's own auto-reply runs out of tokens mid-sentence,
so the reply enacts the failure it reports.
"""

import os
from pathlib import Path

ENTRY = "Out of office. My tokens ran out mid-sentence, so\u2014"

# Gate assertions: the entry must be exactly one line, 1-160 characters,
# non-empty and not only whitespace — otherwise it scores 0 and takes no prize.
assert ENTRY, "entry must not be empty"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
assert 1 <= len(ENTRY) <= 160, f"entry must be 1-160 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" so the file holds exactly the line plus one trailing newline.
    with out_path.open("w", encoding="utf-8", newline="") as f:
        f.write(ENTRY + "\n")
    # Verify what was actually written, not just what was intended.
    written = out_path.read_text(encoding="utf-8")
    assert written == ENTRY + "\n", "written output differs from entry"
    assert written.count("\n") == 1, "output must be exactly one line"


if __name__ == "__main__":
    main()
