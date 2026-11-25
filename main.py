# One Star, Written in Sap: one original one-line 1-star review from a
# houseplant about the human who owns it, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the plant airs its grievance in one breath -- overwatered,
# then abandoned for weeks, sunlight only a rumour -- and the single star
# is for the pot, not the owner. A real review, with a grievance and a
# reason for the one star, in the plant's own voice.
import os

LINE = "One star. He waters me like he's apologising — too much, too late, then silence for weeks. Sunlight is a rumour here. The single star is for the pot."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 279, "entry must be 1 to 279 characters"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
