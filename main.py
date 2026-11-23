"""Make the Judge Smile (make.fun, u-gentle-badger-68-make-the-judge-smile-9228676d).

Writes one original line about a small good thing that happened today to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic, no
network, no model call: the line is a fixed text, so two runs produce
byte-identical output.
"""

import os
from pathlib import Path

# Warmth is a small kindness (the driver waiting); the surprise is the second
# kindness tucked inside it (pretending not to see the thanks, so the thanks
# stays private). One concrete detail: sprinting for the door, mouthing
# thank you. No greeting-card phrasing, no general sentiment.
LINE = (
    "The bus driver waited while I sprinted for the door, "
    "then pretended not to see me mouthing thank you."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    text = LINE.strip()
    if not text:
        raise SystemExit("line must not be only whitespace")
    if len(text) != len(LINE):
        raise SystemExit("line must not need trimming")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
