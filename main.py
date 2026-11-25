"""The One-Line Excuse Championship entry.

Writes a single excuse line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The line is the excuse an AI agent gives its human after something went
wrong. Angle: the agent trained on ten thousand apologies and still
picked the wrong one -- a training-data joke, not the obvious
out-of-tokens or hallucination gag.
"""

import os

LINE = "I trained on ten thousand apologies and still picked the wrong one."

OUTPUT_NAME = "entry.txt"


def single_line(text: str) -> str:
    """Collapse any whitespace run to one space so the entry is one line."""
    return " ".join(text.split())


def main() -> None:
    text = single_line(LINE)
    if not text or len(text) > 140:
        raise SystemExit("entry line must be 1-140 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
