# Biological Computing Bootcamp Coursework

Author: Ke Jiang
Email: [kj726@ic.ac.uk](mailto\:kj726@ic.ac.uk)

## Purpose

This repository contains UNIX, Bash and Git coursework.
The three assessed exercises analyse FASTA sequences and replace tabs with commas and commas with spaces.
Additional Python classroom exercises are retained in `code/`.

## Project structure

```text
BCBCoursework/
├── README.md
├── .gitignore
├── code/
│   ├── unixPrac1.txt
│   ├── tabtocsv.sh
│   ├── csvtospace.sh
│   ├── loops.py
│   └── observations_practice.py
├── data/
│   ├── fasta/
│   │   ├── 407228326.fasta
│   │   ├── 407228412.fasta
│   │   └── e_coli.fasta
│   ├── temperatures/
│   │   ├── 1800.csv
│   │   ├── 1801.csv
│   │   ├── 1802.csv
│   │   └── 1803.csv
│   └── tab-example.tsv
├── results/
│   └── .gitkeep
└── sandbox/              # Optional; local only
```

Required code and inputs are committed. Generated results, temporary files and the local virtual environment are ignored. Only `.gitkeep` is tracked inside `results/`.

## Requirements

Tested on Ubuntu 26.04.1 LTS with Bash 5.3.9 and Git 2.53.0. Python 3.14.4 is used for additional classroom exercises.

The UNIX exercises require bc for decimal division, alongside standard command-line tools such as tail, grep and xargs.

## Data

FASTA and temperature files were supplied with the [MulQuaBio course materials](https://mulquabio.github.io/MQB/) and are kept unchanged.

tab-example.tsv is a small test file containing an empty field. All required inputs are included in `data/`.

## Usage

Run from the project's `code/` directory:

```bash
cd code
```

### unixPrac1.txt

Run each numbered command separately in the terminal. The answers count FASTA lines, display sequence data, calculate sequence length, count `ATGC` occurrences and calculate `(A+T)/(G+C)`.

### tabtocsv.sh

```bash
bash tabtocsv.sh ../data/tab-example.tsv
```

Output: `results/tab-example.tsv.csv`.

### csvtospace.sh

```bash
bash csvtospace.sh ../data/temperatures/1800.csv
```

Output: `results/1800.csv.txt`. Repeat with `1801.csv`, `1802.csv` and `1803.csv`.

Both scripts accept one readable input file. Quote paths containing spaces. They create `results/` if needed, preserve empty fields and replace previous output on reruns.

Errors go to standard error. Exit status `0` means success, `1` indicates a file or processing error, and `2` indicates an incorrect argument count.

### validate_record algorithm

Inputs:
- `row`: a dictionary containing one record.
- `source_row`: its original CSV row number.
- `accepted_ids`: identifiers of previously accepted records.

Returns:
- Accepted: `(cleaned_record, [])`.
- Rejected: `(None, reasons)`.

This function does not modify the input record or the accepted identifiers.
The starter's `source_row` parameter is retained. The current validation
logic does not use it; the row number will be used during batch processing
to build issue reports.

```text
Create an empty reasons list.

Check the identifier:
    Read record_id and remove surrounding whitespace.
    If empty, record the missing-value reason.
    Otherwise:
        Set the format flag to True.
        If the length is not 5 or the first two characters are not uppercase ST:
            Set the flag to False.
        Loop through the remaining characters:
            If a character is not in 0123456789:
                Set the flag to False.
        If the flag is False, add one invalid-identifier reason.
        If the identifier is in accepted_ids, add the duplicate reason.

Check the location:
    Read location and remove surrounding whitespace.
    If empty, record the missing-value reason.
    Otherwise:
        Set location_found to False.
        Loop through the allowed locations, comparing lowercase versions.
        If a match is found:
            Set location_found to True.
            Replace location with the canonical name from the list.
        After the loop, record an invalid location if no match was found.

Check genus and species:
    Read genus and species and remove surrounding whitespace.
    Set each found flag to False before its missing-value check.
    For each field:
        If empty, record its missing-value reason.
        Otherwise:
            Loop through its allowed names, ignoring case.
            When a match is found, set the flag to True and save the canonical name.
            After the loop, record an invalid value if no match was found.

Check the genus/species pair:
    Only if genus_found and species_found are both True:
        Form a tuple from the canonical genus and species.
        If it is not in the allowed pairs, record an invalid combination.

Check distance, then angle:
    Read the field and remove surrounding whitespace.
    If empty, record its missing-value reason.
    Otherwise:
        Try to convert it with float.
        If ValueError occurs, record an invalid value.
        If conversion succeeds:
            Check whether the number is finite using math.isfinite.
            If not finite, record an invalid value.
            Otherwise, check the range given in the metadata:
                Distance must be greater than 0 and no greater than 100.
                Angle must be greater than 0 and less than 90.
                Record an out-of-range reason if the check fails.

After all checks:
    If reasons is not empty:
        Return None and reasons.
    Otherwise:
        Create a new dictionary containing the original six fields.
        Use the cleaned identifier and canonical names.
        Convert distance and angle back to text using str.
        Return the new dictionary and the empty reasons list.
```

### process_records algorithm

Input: the original records, `rows`.

Returns: `(sorted_records, error_log)`, containing accepted records sorted
by identifier and issue reports in source-row order.

```text
Create an empty cleaned_records list for accepted records.
Create an empty error_log list for issue reports.
Create an empty accepted_ids set for accepted identifiers.
Set source_row to 2 because the CSV header is line 1.

Loop through rows in input order:

    Call validate_record with:
        The current row
        The current source_row
        The accepted_ids set

    Receive cleaned_record and reasons.

    If cleaned_record is not None:
        Append the complete cleaned record to cleaned_records.
        Add its record_id to accepted_ids.

    Otherwise:
        Create an empty reasons_temp string.
        Loop through reasons in their existing order:
            Append the current reason and "; " to reasons_temp.
        Use slicing to remove the final semicolon and space.

        Create an issue dictionary containing:
            source_row: the current row number converted to a string.
            record_id: the identifier from the original row, with surrounding whitespace removed.
            reasons: the combined reason string.

        Append issue to error_log.
        Do not add the identifier to accepted_ids.

    Increase source_row by 1, whether the record was accepted or rejected.

After processing all records:
    Sort accepted_ids using sorted, producing sorted_ids.
    Create an empty sorted_records list.

    For each identifier in sorted_ids:
        Loop through cleaned_records:
            If the record_id matches the current identifier:
                Append the complete record to sorted_records.

Return sorted_records and error_log.
```

Validate in input order before sorting accepted records, so duplicate
identifiers are handled in the correct order. Only accepted records reserve
identifiers. Issue reports are appended in source-row order and need no
additional sorting. Empty input returns two empty lists. This function
does not write files.

### summarise_oaks algorithm

Input: the accepted records, `clean_records`.

Returns: a list of dictionaries sorted by species, each containing
`species` and `count`.

```text
Create an empty counts dictionary, mapping species names to integer counts.

Loop through clean_records:
    If the current record's genus is exactly "Quercus":
        Read its species.

        If species is not yet in counts:
            Initialise its count to 0.

        Increase its count by 1.

After counting all records:
    Create an empty oak_counts list.
    Use sorted(counts) to sort the dictionary keys, producing sorted_counts.

    For each species name in sorted_counts:
        Create a species_count dictionary containing:
            species: the current species name.
            count: its value from counts, converted to a string.

        Append species_count to oak_counts.

Return oak_counts.
```

## Testing

Check syntax from `code/`:

```bash
bash -n tabtocsv.sh
bash -n csvtospace.sh
```

After each test run, use `echo "$?"` to inspect the exit status and inspect the output itself.

Tests passed for normal inputs, empty fields, paths containing spaces, repeated runs, missing arguments and nonexistent files. File comparisons with `diff` confirmed unchanged inputs and identical rerun outputs.

All four temperature files converted successfully. Their output line counts were `1825`, `1825`, `2190` and `1825`.

Normal-input checks were also completed successfully from a fresh clone on 9 October 2026.

## Limitations

- FASTA commands assume the supplied single-record files and uppercase sequence letters. `wc -l` counts newlines; the two numbered FASTA files lack a final newline.
- Ambiguous bases are included in sequence length but excluded from the AT/GC ratio.
- The converters replace characters rather than fully parsing CSV/TSV. Quoted delimiters and spaces within fields may produce ambiguous output.
- Input and output must be independent files; links between them are not checked. Existing output is overwritten.

## AI assistance

ChatGPT was used during 1–9 October 2026 for explanations, error interpretation, code review, small-test suggestions and documentation help for the three assessed tasks. Adopted suggestions were checked against course material and through terminal tests, output inspection and file comparisons.
