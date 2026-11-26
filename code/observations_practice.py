"""Load observations, parse counts and summarise one requested site.

Exact duplicate records are counted once. Missing counts are counted
separately from known values, including observed zeros.
"""

import csv


def load_observations(path):
    """Read a UTF-8 CSV file into a list of row dictionaries."""
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def parse_count(count_text):
    """Return a non-negative integer, or None for empty text.

    Raise ValueError for non-text input, invalid integer text
    or a negative count.
    """
    if not isinstance(count_text, str):
        raise ValueError("Count must be text")

    if count_text == "":
        return None

    count = int(count_text)

    if count < 0:
        raise ValueError("Count cannot be negative")

    return count


# Algorithm for summarise_site:
# Input: a list of row dictionaries and a non-empty text site.
# Validate every row before filtering or removing exact duplicates.
# Keep one copy of each (site, date, count) record.
# For the requested site, sum known counts and count missing observations.
# If no known count exists, return None for the total.
# Empty input or an absent site returns (None, 0).
# Output: (known_total, missing_count), without modifying the input.


def summarise_site(rows, site):
    """Return (known_total, missing_count) for one requested site.

    Require a list of dictionaries with exactly the text fields
    site, date and count. Site and date must be non-empty.
    Validate counts using parse_count, including rows for other sites.

    Count exact duplicate records once. Return None for the total
    when no known count exists. Do not modify the input rows.
    Raise ValueError for invalid input.
    """
    if not isinstance(rows, list):
        raise ValueError("Rows must be a list")

    if not isinstance(site, str):
        raise ValueError("Site must be text")

    if site == "":
        raise ValueError("Site cannot be empty")

    unique = []

    # Validate every row, including duplicates and rows for other sites.
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Each row must be a dictionary")

        if "site" not in row:
            raise ValueError("Missing site")
        if "date" not in row:
            raise ValueError("Missing date")
        if "count" not in row:
            raise ValueError("Missing count")

        if len(row) != 3:
            raise ValueError("Row has extra fields")

        if not isinstance(row["site"], str):
            raise ValueError("Site must be text")
        if row["site"] == "":
            raise ValueError("Site cannot be empty")

        if not isinstance(row["date"], str):
            raise ValueError("Date must be text")
        if row["date"] == "":
            raise ValueError("Date cannot be empty")

        # This also checks that count is text and rejects invalid values.
        parse_count(row["count"])

        # Valid rows have exactly three fields, so dictionary equality
        # identifies exact (site, date, count) duplicates.
        if row not in unique:
            unique.append(row)

    known_total = 0
    missing_count = 0
    known_count = 0

    for row in unique:
        if row["site"] == site:
            count = parse_count(row["count"])

            if count is None:
                missing_count += 1
            else:
                known_total += count
                known_count += 1

    # Observed zero is known; only the absence of known counts gives None.
    if known_count == 0:
        known_total = None

    return known_total, missing_count

def suggested_total(rows, site):
    """Deliberately faulty teaching example; not the correct summary."""
    total = 0
    seen = set()

    for row in rows:
        record = (row["site"], row["date"], row["count"])
        if record in seen:
            continue
        seen.add(record)

        if row["site"] == site and row["count"] != "":
            total += int(row["count"])

    return total

if __name__ == "__main__":
    rows = load_observations("data/bootcamp_observations.csv")

    # Collect distinct sites and report them in a consistent order.
    sites = sorted({row["site"] for row in rows})

    for site in sites:
        known_total, missing_count = summarise_site(rows, site)
        print(
            f"Site {site}: known_total={known_total}, "
            f"missing_count={missing_count}"
        )