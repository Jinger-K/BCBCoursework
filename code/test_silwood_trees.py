from clean_silwood_trees import validate_record, process_records, summarise_oaks

# Test 1: Accept a valid record and return the expected cleaned values
valid_record = {
    "record_id":"ST001",
    "location":"Manor House",
    "genus":"Quercus",
    "species":"robur",
    "distance_m":"30",
    "angle_degrees":"30"
}

expected_record = {
    "record_id": "ST001",
    "location": "Manor House",
    "genus": "Quercus",
    "species": "robur",
    "distance_m": "30.0",
    "angle_degrees": "30.0",
}

cleaned_record, reasons = validate_record(valid_record, 2, set())
assert reasons == []
assert cleaned_record == expected_record

print("Valid-record test passed.")

# Test 2: Remove surrounding spaces and standardise case
messy_record = {
    "record_id": " ST001 ",
    "location": " manor house ",
    "genus": " QUERCUS ",
    "species": " ROBUR ",
    "distance_m": " 30 ",
    "angle_degrees": "30",
}

cleaned_record, reasons = validate_record(messy_record, 2, set())

assert reasons == []
assert cleaned_record == expected_record

print("Text-cleaning test passed.")

# Test 3: Reject missing values in each required field
missing_cases = [
    ("record_id", "missing record_id"),
    ("location", "missing location"),
    ("genus", "missing genus"),
    ("species", "missing species"),
    ("distance_m", "missing distance_m"),
    ("angle_degrees", "missing angle_degrees"),
]

for field, expected_reason in missing_cases:
    for missing_value in ["", "   "]:
        # Build a separate record by copying each key-value pair
        missing_record = {}

        for key in valid_record:
            missing_record[key] = valid_record[key]

        missing_record[field] = missing_value

        cleaned_record, reasons = validate_record(
            missing_record, 2, set()
        )

        assert cleaned_record is None
        assert reasons == [expected_reason]

print("Missing-value tests passed.")


# Test 4: Reject invalid identifiers and unrecognised text values
invalid_text_cases = [
    ("record_id", "st001", "invalid record_id"),
    ("record_id", "ST01", "invalid record_id"),
    ("record_id", "ST0001", "invalid record_id"),
    ("record_id", "ST0A1", "invalid record_id"),
    ("record_id", "AB001", "invalid record_id"),
    ("location", "Unknown Place", "invalid location"),
    ("location", "Manor Hous", "invalid location"),
    ("genus", "Quercuss", "invalid genus"),
    ("species", "roburr", "invalid species"),
]

for field, invalid_value, expected_reason in invalid_text_cases:
    # Build a separate valid record for each test case
    invalid_record = {}

    for key in valid_record:
        invalid_record[key] = valid_record[key]

    # Replace one field with an invalid value
    invalid_record[field] = invalid_value

    cleaned_record, reasons = validate_record(
        invalid_record, 2, set()
    )

    # Reject the record with exactly the expected reason
    assert cleaned_record is None
    assert reasons == [expected_reason]

print("Invalid-text tests passed.")

# Test 5: Accept permitted taxon pairs and reject invalid combinations
taxon_cases = [
    ("Quercus", "robur", []),
    ("Quercus", "petraea", []),
    ("Acer", "pseudoplatanus", []),
    ("Betula", "pendula", []),
    ("Fagus", "sylvatica", []),
    ("Fraxinus", "excelsior", []),
    ("Quercus", "pseudoplatanus", ["invalid genus/species combination"]),
    ("Acer", "robur", ["invalid genus/species combination"]),
]

for genus, species, expected_reasons in taxon_cases:
    test_record = {}

    for key in valid_record:
        test_record[key] = valid_record[key]

    test_record["genus"] = genus
    test_record["species"] = species

    cleaned_record, reasons = validate_record(test_record, 2, set())

    assert reasons == expected_reasons

    if expected_reasons == []:
        assert cleaned_record is not None
        assert cleaned_record["genus"] == genus
        assert cleaned_record["species"] == species
    else:
        assert cleaned_record is None

print("Taxon-pair tests passed.")

# Test 6: Reject non-numeric and non-finite measurements
measurement_error = [
    ("distance_m", "invalid distance_m"),
    ("angle_degrees", "invalid angle_degrees"),
]

invalid_measurements = ["many", "nan", "inf", "-inf"]

for field, expected_reason in measurement_error:
    for invalid_value in invalid_measurements:

        test_record = {}

        for key in valid_record:
            test_record[key] = valid_record[key]

        test_record[field] = invalid_value

        cleaned_record, reasons = validate_record(
            test_record, 2, set()
        )

        assert cleaned_record is None
        assert reasons == [expected_reason]

print("Invalid-measurement tests passed.")


# Test 7: Check valid measurements, range limits and boundary values
range_cases = [
    ("distance_m", "-1", ["distance_m out of range"]),
    ("distance_m", "0", ["distance_m out of range"]),
    ("distance_m", "0.5", []),
    ("distance_m", "30.5", []),
    ("distance_m", "100", []),
    ("distance_m", "100.1", ["distance_m out of range"]),
    ("angle_degrees", "-1", ["angle_degrees out of range"]),
    ("angle_degrees", "0", ["angle_degrees out of range"]),
    ("angle_degrees", "0.5", []),
    ("angle_degrees", "45.5", []),
    ("angle_degrees", "89.9", []),
    ("angle_degrees", "90", ["angle_degrees out of range"]),
    ("angle_degrees", "91", ["angle_degrees out of range"]),
]

for field, value, expected_reasons in range_cases:
    test_record = {}

    for key in valid_record:
        test_record[key] = valid_record[key]

    test_record[field] = value

    cleaned_record, reasons = validate_record(test_record, 2, set())

    assert reasons == expected_reasons

    if expected_reasons == []:
        assert cleaned_record is not None

        assert isinstance(cleaned_record[field], str)
        assert float(cleaned_record[field]) == float(value)
    else:
        assert cleaned_record is None

print("Measurement-range tests passed.")

# Test 8: Collect all applicable reasons in the required order
multiple_error_record = {}

for key in valid_record:
    multiple_error_record[key] = valid_record[key]

multiple_error_record["record_id"] = "st001"
multiple_error_record["location"] = ""
multiple_error_record["distance_m"] = "-1"
multiple_error_record["angle_degrees"] = "none"

expected_reasons = [
    "invalid record_id",
    "missing location",
    "distance_m out of range",
    "invalid angle_degrees",
]

cleaned_record, reasons = validate_record(
    multiple_error_record, 2, set()
)

assert cleaned_record is None
assert reasons == expected_reasons

print("Multiple-error test passed.")

# Test 9: Reject accepted identifiers and continue checking other fields
accepted_ids = {"ST001"}


cleaned_record, reasons = validate_record(
    valid_record, 3, accepted_ids
)

assert cleaned_record is None
assert reasons == ["duplicate record_id"]
assert accepted_ids == {"ST001"}


duplicate_error_record = {}

for key in valid_record:
    duplicate_error_record[key] = valid_record[key]

duplicate_error_record["record_id"] = " ST001 "
duplicate_error_record["distance_m"] = "-1"

cleaned_record, reasons = validate_record(
    duplicate_error_record, 4, accepted_ids
)

assert cleaned_record is None
assert reasons == [
    "duplicate record_id",
    "distance_m out of range",
]
assert accepted_ids == {"ST001"}

print("Duplicate-identifier tests passed.")





# Test 10: Process records in order and produce the required output lists
processing_cases = [
    ("ST003", "Manor House", "-1"),
    ("ST003", "Manor House", "30"),
    ("ST001", "Manor House", "30"),
    (" ST003 ", "", "30"),
]

test_rows = []

for record_id, location, distance in processing_cases:
    test_record = {}

    for key in valid_record:
        test_record[key] = valid_record[key]

    test_record["record_id"] = record_id
    test_record["location"] = location
    test_record["distance_m"] = distance

    test_rows.append(test_record)

cleaned_records, error_log = process_records(test_rows)

expected_cleaned_records = [
    {
        "record_id": "ST001",
        "location": "Manor House",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "30.0",
        "angle_degrees": "30.0",
    },
    {
        "record_id": "ST003",
        "location": "Manor House",
        "genus": "Quercus",
        "species": "robur",
        "distance_m": "30.0",
        "angle_degrees": "30.0",
    },
]

expected_error_log = [
    {
        "source_row": "2",
        "record_id": "ST003",
        "reasons": "distance_m out of range",
    },
    {
        "source_row": "5",
        "record_id": "ST003",
        "reasons": "duplicate record_id; missing location",
    },
]

assert cleaned_records == expected_cleaned_records
assert error_log == expected_error_log

print("Record-processing tests passed.")




# Test 11: Count exact oak matches by species and sort the summary
oak_cases = [
    ("ST001", "Quercus", "robur"),
    ("ST002", "Betula", "pendula"),
    ("ST003", "Quercus", "petraea"),
    ("ST004", "Quercus", "robur"),
    ("ST005", "Quercuss", "robur"),
]

oak_test_records = []

for record_id, genus, species in oak_cases:
    # Build a separate record for each case
    test_record = {}

    for key in valid_record:
        test_record[key] = valid_record[key]

    test_record["record_id"] = record_id
    test_record["genus"] = genus
    test_record["species"] = species

    oak_test_records.append(test_record)

# Call the summary directly to check that a near-match name is excluded
oak_summary = summarise_oaks(oak_test_records)

expected_oak_summary = [
    {"species": "petraea", "count": "1"},
    {"species": "robur", "count": "2"},
]

assert oak_summary == expected_oak_summary

print("Oak-counting and sorting tests passed.")



# Test 12: Include only represented oak species and handle no-oak input

# valid_record contains one Quercus robur record
assert summarise_oaks([valid_record]) == [
    {"species": "robur", "count": "1"},
]

# An accepted non-oak record must produce an empty oak summary
non_oak_record = {}

for key in valid_record:
    non_oak_record[key] = valid_record[key]

non_oak_record["genus"] = "Betula"
non_oak_record["species"] = "pendula"

assert summarise_oaks([non_oak_record]) == []

# No accepted records must also produce an empty summary
assert summarise_oaks([]) == []

print("Represented-species and no-oak tests passed.")