"""Check count conversion, site summaries and input protection."""

from observations_practice import (
    load_observations,
    parse_count,
    summarise_site,
    suggested_total,
)


# Count conversion: ordinary values, observed zero and missing data.
assert parse_count("2") == 2
assert parse_count("0") == 0
assert parse_count("") is None

# Invalid counts must raise ValueError, not silently succeed.
for bad_count in ["-1", "many", 2]:
    try:
        parse_count(bad_count)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid count accepted: {bad_count!r}")


# Sum only the requested site's valid, unique observations.
unique_rows = [
    {"site": "A", "date": "2026-10-01", "count": "2"},
    {"site": "A", "date": "2026-10-02", "count": "3"},
    {"site": "B", "date": "2026-10-01", "count": "9"},
]
assert summarise_site(unique_rows, "A") == (5, 0)


# Missing observations differ from a genuinely observed zero.
missing_rows = [
    {"site": "C", "date": "2026-10-01", "count": ""},
    {"site": "C", "date": "2026-10-02", "count": ""},
]
zero_rows = [
    {"site": "D", "date": "2026-10-01", "count": "0"},
]

assert summarise_site(missing_rows, "C") == (None, 2)
assert summarise_site(zero_rows, "D") == (0, 0)

# Empty input and an absent site have no known total.
assert summarise_site([], "A") == (None, 0)
assert summarise_site(unique_rows, "Z") == (None, 0)


# Repeated nonzero and missing records must each be counted once.
assert summarise_site(
    unique_rows + [unique_rows[0]], "A"
) == (5, 0)

assert summarise_site(
    missing_rows + [missing_rows[0]], "C"
) == (None, 2)


# Check the ordinary CSV file.
rows = load_observations("data/bootcamp_observations.csv")
assert summarise_site(rows, "A") == (2, 1)
assert summarise_site(rows, "B") == (0, 0)
assert summarise_site(rows, "Z") == (None, 0)

# The deliberately faulty example still passes these ordinary checks.
assert suggested_total(rows, "A") == 2
assert suggested_total(rows, "B") == 0

boundary_rows = load_observations(
    "data/bootcamp_observations_boundary.csv"
)
assert summarise_site(boundary_rows, "C") == (None, 2)
assert summarise_site(boundary_rows, "D") == (0, 0)


def expect_summary_error(test_rows, site="A"):
    """Require ValueError while allowing unexpected exceptions to surface."""
    try:
        summarise_site(test_rows, site)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError, but the call succeeded")


# Check invalid CSV rows separately so one error cannot hide another.
# The default request is A, so invalid rows for other sites must also fail.
invalid_rows = load_observations(
    "data/bootcamp_observations_invalid.csv"
)
for invalid_row in invalid_rows:
    expect_summary_error([invalid_row])


# Missing or extra fields.
expect_summary_error([
    {"site": "A", "count": "2"},
])
expect_summary_error([
    {
        "site": "A",
        "date": "2026-10-01",
        "count": "2",
        "extra": "x",
    },
])

# Site and date must be non-empty text.
expect_summary_error([
    {"site": "", "date": "2026-10-01", "count": "2"},
])
expect_summary_error([
    {"site": 2, "date": "2026-10-01", "count": "2"},
])
expect_summary_error([
    {"site": "A", "date": "", "count": "2"},
])
expect_summary_error([
    {"site": "A", "date": 2, "count": "2"},
])

# Counts must be text accepted by parse_count.
for bad_count in [2, "-1", "many"]:
    expect_summary_error([
        {"site": "A", "date": "2026-10-01", "count": bad_count},
    ])

# Invalid data must be rejected even when it belongs to another site.
expect_summary_error([
    {"site": "A", "date": "2026-10-01", "count": "2"},
    {"site": "B", "date": "2026-10-01", "count": "many"},
])

# Check the row container, individual row type and requested site.
expect_summary_error(["not a row dictionary"])
expect_summary_error([None])
expect_summary_error(None)
expect_summary_error({})
expect_summary_error(rows, "")
expect_summary_error(rows, 2)


# Copy each dictionary so changes to field values would be detectable.
original_rows = [row.copy() for row in rows]
summarise_site(rows, "A")
assert rows == original_rows

# Also check input preservation when duplicate records are supplied.
duplicate_rows = unique_rows + [unique_rows[0]]
original_duplicate_rows = [row.copy() for row in duplicate_rows]
summarise_site(duplicate_rows, "A")
assert duplicate_rows == original_duplicate_rows

# Synthetic observations using Silwood place names.
# These are invented test records, not real survey data.
new_rows = [
    {"site": "Pound Hill", "date": "2026-10-23", "count": "4"},
    {"site": "Pound Hill", "date": "2026-10-24", "count": ""},
    {"site": "Pound Hill", "date": "2026-10-25", "count": "6"},
    {"site": "Pound Hill", "date": "2026-10-23", "count": "4"},
    {"site": "Silwood Park", "date": "2026-10-23", "count": "0"},
    {"site": "Silwood Park", "date": "2026-10-24", "count": ""},
    {"site": "Silwood Park", "date": "2026-10-24", "count": ""},
]

# Hand-worked expectations:
# Pound Hill: 4 + 6 = 10, one missing; the repeated count of 4 is ignored.
# Silwood Park: one known zero, one missing; the repeated missing row is ignored.
assert summarise_site(new_rows, "Pound Hill") == (10, 1)
assert summarise_site(new_rows, "Silwood Park") == (0, 1)