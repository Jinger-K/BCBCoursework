# Biological Computing Bootcamp Coursework

Author: Ke Jiang
Email: [kj726@ic.ac.uk](mailto\:kj726@ic.ac.uk)

## Purpose

This repository contains coursework and practical exercises from the Biological Computing Bootcamp.

Assignment 1 covers UNIX commands, FASTA analysis and delimiter conversion.
Assignment 2 validates synthetic tree-survey records and produces cleaned data, issue reports and oak counts.
Assignment 3 calculates tree heights using fixed-input and command-line R scripts, and compares plant species richness and abundance among cultivation treatments at Pound Hill.

Additional Python and R classroom exercises are kept in `code/`.

## Project structure

```text
BCBCoursework/
├── README.md
├── .gitignore
├── Feedback/
│   ├── assignment-1-2026.md
│   └── assignment-2-2026.md
├── code/
│   ├── TreeHeight.R
│   ├── basic_io.R
│   ├── basic_plotting_commands_in_R
│   ├── boilerplate.R
│   ├── break.R
│   ├── browse.R
│   ├── clean_silwood_trees.py
│   ├── control_flow.R
│   ├── csvtospace.sh
│   ├── data_wrang.R
│   ├── data_wrang_tidy.R
│   ├── debugme.py
│   ├── get_TreeHeight.R
│   ├── loops.py
│   ├── next.R
│   ├── observations_practice.R
│   ├── observations_practice.py
│   ├── pound_hill_analysis.R
│   ├── r_conditionals.R
│   ├── run_get_TreeHeight.sh
│   ├── tabtocsv.sh
│   ├── test_silwood_trees.py
│   ├── try.R
│   └── unixPrac1.txt
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
│   ├── pound_hill_data.csv
│   ├── pound_hill_meta_data.csv
│   ├── silwood_trees_metadata.md
│   ├── silwood_trees_raw.csv
│   ├── tab-example.tsv
│   └── trees.csv
└── results/
    └── .gitkeep
```

Required code and inputs are committed. Generated results, temporary files and the local virtual environment are ignored. Only `.gitkeep` is tracked inside `results/`.

## Requirements

Tested on Ubuntu 26.04.1 LTS with Bash 5.3.9 and Git 2.53.0. Python 3.14.4 is used for additional classroom exercises.

The UNIX exercises require bc for decimal division, alongside standard command-line tools such as tail, grep and xargs.

The Assignment 2 cleaner and test script require Python 3 and use only the standard library. No additional Python packages are needed.

The Assignment 3 analyses require R. The R analyses were tested with R 4.5.2 (2025-10-31).
The tree-height scripts use base R only. The Pound Hill analysis requires
`reshape2`, `dplyr` and `ggplot2`.

Install missing packages from an R session:

```r
install.packages(c("reshape2", "dplyr", "ggplot2"))

## Data

FASTA and temperature files were supplied with the [MulQuaBio course materials](https://mulquabio.github.io/MQB/) and are kept unchanged.

tab-example.tsv is a small test file containing an empty field. All required inputs are included in `data/`.

The synthetic tree survey and its metadata were supplied with the MulQuaBio practical.
They are stored unchanged as `data/silwood_trees_raw.csv` and
`data/silwood_trees_metadata.md`.

The supplied tree-height table is stored unchanged as `data/trees.csv`.
It contains 120 records with the columns `Species`, `Distance.m` and `Angle.degrees`.

The supplied Pound Hill files are stored unchanged as
`data/pound_hill_data.csv` and `data/pound_hill_meta_data.csv`.
The metadata specifies that blank species counts represent observed absences, which are converted to zero during analysis.

## Usage

For the Assignment 1 commands below, start from the project root and enter `code/`:

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

### Assignment 2: Tree-survey validation

Run the cleaner from the project root. If the terminal is still inside `code/`,
run `cd ..` first.

```bash
python3 code/clean_silwood_trees.py
```

The program reads `data/silwood_trees_raw.csv` and creates or replaces:

| Output | Contents |
| --- | --- |
| `results/silwood_trees_clean.csv` | Accepted records, sorted by `record_id`. |
| `results/silwood_tree_issues.csv` | Rejected source rows, cleaned identifiers and ordered reasons. |
| `results/oak_species_counts.csv` | Accepted oak counts by species, sorted by species. |

The program creates `results/` when needed and leaves the raw survey unchanged.
The generated files are excluded from Git.

The algorithms below describe the three implemented functions.

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

### Assignment 3: Tree-height calculation

Run all commands from the project root.

The fixed-input script reads only `data/trees.csv` and writes
`results/TreeHts.csv`:

```bash
Rscript code/TreeHeight.R
```

It can also be run from an R session started at the project root:

```r
source("code/TreeHeight.R")
```

The generalised script accepts exactly one readable CSV path with the same
three required columns:

```bash
Rscript code/get_TreeHeight.R data/trees.csv
```

For this input, the output is `results/trees_treeheights.csv`.
The shell wrapper runs this command and returns a non-zero exit status
if it fails:

```bash
bash code/run_get_TreeHeight.sh
```

Both R scripts calculate
`height_m = Distance.m * tan(Angle.degrees * pi / 180)`.
They preserve input record order and produce the four columns
`Species`, `Distance.m`, `Angle.degrees` and `height_m`.
They create `results/` if needed and replace existing results on reruns.

### Assignment 3: Pound Hill analysis

Run from the project root:

```bash
Rscript code/pound_hill_analysis.R
```

The script reads the supplied data and metadata, converts blank species
counts to observed zeros, reshapes the data to long form, and checks counts.

Richness is calculated separately for each quadrat as the number of
species with `Count > 0`. Quadrat richness is then averaged within each
plot, so plots with more sampled quadrats do not receive greater weight
in the treatment comparison.

Outputs:

| Output | Contents |
| --- | --- |
| `results/pound_hill_plot_richness.csv` | One row per plot, containing `Cultivation`, `Block`, `Plot` and `MeanRichness`. |
| `results/pound_hill_plot_richness.pdf` | Individual plot-level mean richness values by cultivation treatment, coloured by block. |

The script also calculates total abundance within each quadrat and its mean within each plot. The abundance summary is printed to the terminal and compared with richness in the script comments.

The figure shows one mean quadrat richness value per plot, with colours identifying blocks. May has the highest typical richness, while March and October are lower. Plot values vary within treatments and overlap between treatments; the figure alone does not establish causation.


## Testing

### Assignment 1

Check syntax from `code/`:

```bash
bash -n tabtocsv.sh
bash -n csvtospace.sh
```

After each test run, use `echo "$?"` to inspect the exit status and inspect the output itself.

Tests passed for normal inputs, empty fields, paths containing spaces, repeated runs, missing arguments and nonexistent files. File comparisons with `diff` confirmed unchanged inputs and identical rerun outputs.

All four temperature files converted successfully. Their output line counts were `1825`, `1825`, `2190` and `1825`.

Normal-input checks were also completed successfully from a fresh clone on 9 October 2026.

### Assignment 2

Run the test script from the project root:

```bash
python3 code/test_silwood_trees.py
```

The script uses constructed records and `assert` checks without changing the survey.
All 12 test sections passed. They cover text cleaning, missing and unrecognised
values, taxon pairs, invalid and out-of-range measurements, duplicate identifiers,
multiple rejection reasons, record processing, and oak summaries.

One useful test checks that `nan` and `inf` are rejected as invalid measurements. This detects a validation error where successful conversion to a number is incorrectly treated as sufficient for acceptance.

Repeated-run consistency and the unchanged raw input were checked manually.
Import behaviour, automatic creation of `results/`, and output contents were
also checked separately from the function tests.

### Assignment 3

All analyses were run independently from the project root and rerun
successfully.

- Tree heights: outputs had the required four columns and 120 records
  in input order. The first record was checked against the formula,
  and a separate 8 m, 45-degree measurement returned 8 m. Reruns produced
  identical CSV files. Command-line error cases and numeric boundaries
  were checked, and interactive debugging with `browser()` was completed.
- Pound Hill: the richness CSV contained 12 plots, each appearing once,
  with four plots per treatment. The saved PDF was inspected, and rerunning
  produced an identical CSV.


## Limitations

### Assignment 1
- FASTA commands assume the supplied single-record files and uppercase sequence letters. `wc -l` counts newlines; the two numbered FASTA files lack a final newline.
- Ambiguous bases are included in sequence length but excluded from the AT/GC ratio.
- The converters replace characters rather than fully parsing CSV/TSV. Quoted delimiters and spaces within fields may produce ambiguous output.
- Input and output must be independent files; links between them are not checked. Existing output is overwritten.

### Assignment 2

- Source-row numbering assumes one record per line, with no blank lines between records.
- Each input record must contain all six fields as strings. Empty cells are handled, but structurally missing fields that CSV reading represents as `None` are not supported.
- The cleaner supports only the column layout, locations and taxon pairs specifies in the supplied metadata.

The supplied survey was checked and satisfies these assumptions, so these limitations
do not affect this dataset.

### Assignment 3: Tree-height calculation

- Measurements must satisfy the specified numeric, finite-value and range checks. The scripts validate inputs rather than clean invalid records.
- The generalised script uses the input basename to name its output. Inputs from different directories with the same basename target the same result file, so a later run replaces the earlier result.

### Assignment 3: Pound Hill analysis

- The conversion of blank counts to zero is justified by this dataset's metadata and should not be assumed appropriate for other datasets.
- Plot 12 in the May treatment, Block d, contains Q1, Q2 and Q4 only. Its mean is calculated from these three recorded quadrats. Q3 is not added as a zero-valued quadrat; the supplied files do not explain why it was not recorded.
- The figure describes differences and variation among plots. It does not by itself establish a causal effect of cultivation timing.

## AI assistance

For Assignment 1, ChatGPT was used during 1–9 October 2026 for explanations, error interpretation, code review, small-test suggestions and documentation help for the three assessed tasks. Adopted suggestions were checked against course material and through terminal tests, output inspection and file comparisons.

For Assignment 2, I used ChatGPT as a tutor during 13–18 October 2026
to explain Python concepts and task requirements, discuss my algorithm ideas,
understand errors, suggest small test cases, and help organise and clarify
the README documentation. I checked the guidance against
the course materials and metadata, traced examples by hand, and ran my tests
and inspected the outputs.

For Assignment 3, I used ChatGPT during 19–23 October 2026 for explanations of R syntax and task requirements, help understanding errors, hints when stuck, suggestions for small checks, and README documentation help.
I checked adopted suggestions against the MQB materials and metadata, inspected intermediate tables and the figure, and independently ran the scripts, boundary checks and repeated-run comparisons.