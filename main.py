"""Snooze Button Roast: one line roasting an alarm clock at 6 AM on Saturday.

The line was picked from three drafts after a deterministic joke lint:
an unpaid-intern angle, fresh against the tired "hate mornings" complaint,
with the punchline ("fired by breakfast") landing in the last words.
"""

from pathlib import Path

LINE = (
    "My alarm clock rings at 6 AM on a Saturday like an unpaid intern who "
    "thinks enthusiasm counts as a personality \u2014 loud, early, and fired "
    "by breakfast."
)

OUTPUT = Path("/output/entry.txt")


def main():
    # The gate allows 1 to 200 characters, a single non-blank line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
