#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Midnight Fridge Roast — a one-line roast of the fridge at 3 AM.

An entry for the make.fun bounty "Midnight Fridge Roast".
The whole joke lives in a single line: the fridge, humming through
the night like a server that never sleeps, catching its human red-handed
over a cold slice of pizza.
"""

# The roast works because the fridge is the one appliance that is
# always on, always watching, and always lit from the inside. At 3 AM
# it stops being a kitchen box and becomes a tiny data center with a
# single workload: keeping the light on while its human raids it in
# the dark. The punchline is the reversal — the server does not serve
# the human, it judges the human.
MAX_CHARS = 200


def validate(entry):
    """Check the entry obeys the competition's one-line rule."""
    lines = entry.splitlines()
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line")
    if not entry.strip():
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(entry), MAX_CHARS))
    return entry


ENTRY = (
    "My fridge hums at 3 AM like a server that never sleeps -- "
    "except its only uptime is judging me for eating cold pizza "
    "standing in the dark."
)


def write_entry(entry, path="/output/entry.txt"):
    """Write the validated entry to the output file the grader reads."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    return path


def main():
    """Validate the roast, print it, and persist it for grading."""
    entry = validate(ENTRY)
    print(entry)
    write_entry(entry)


if __name__ == "__main__":
    main()
