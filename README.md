# Biological Computing Bootcamp Coursework

Author: Ke Jiang
Email: [kj726@ic.ac.uk](mailto\:kj726@ic.ac.uk)

## Purpose

This repository contains coursework and practical exercises from the Biological Computing Bootcamp.

Assignment 1 covers UNIX commands, FASTA analysis and delimiter conversion.
Assignment 2 validates synthetic tree-survey records and produces cleaned data, issue reports and oak counts.
Assignment 3 calculates tree heights using fixed-input and command-line R scripts, and compares plant species richness and abundance among cultivation treatments at Pound Hill.

Additional Shell, Python and R classroom exercises are kept in `code/`.

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
```

##  Data

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

### unixPrac1.txt

This file contains five numbered UNIX commands with explanations for
inspecting the supplied FASTA files.

From the repository root, enter `code/`:

```bash
cd code
```

Run each numbered command in `unixPrac1.txt` separately in the terminal.
The commands read the three supplied files through `../data/fasta/`.
Do not run the answer file as a shell script.

The commands count newline characters, display the E. coli sequence
without its header, calculate sequence length, count `ATGC` occurrences,
and calculate `(A+T)/(G+C)`. Results are printed to the terminal;
no output files are created.

After completing the FASTA commands, return to the repository root:

```bash
cd ..
```

### tabtocsv.sh

Run from the repository root:

```bash
bash code/tabtocsv.sh data/tab-example.tsv
```

The script accepts exactly one readable tab-delimited input file.
Quote input paths containing spaces.

It replaces tabs with commas and writes
`results/<input-filename>.csv`. For the example above, the output is
`results/tab-example.tsv.csv`.

The script creates `results/` if needed, preserves empty fields,
leaves the input unchanged and overwrites its previous output on reruns.

Errors are written to standard error without reporting success.
Exit status `0` indicates success, `1` indicates a file or processing
error, and `2` indicates an incorrect argument count.

This script requires Bash and the standard command-line tools
`basename`, `mkdir` and `tr`.

### csvtospace.sh

Run from the repository root:

```bash
bash code/csvtospace.sh data/temperatures/1800.csv
```

Repeat with `1801.csv`, `1802.csv` and `1803.csv`.

The script accepts exactly one readable CSV input path.
Quote paths containing spaces.

It replaces commas with spaces and writes
`results/<input-filename>.txt`. For the example above, the output is
`results/1800.csv.txt`.

The script creates `results/` if needed, preserves empty fields as
repeated spaces, leaves the input unchanged and overwrites previous
output on reruns.

Errors are written to standard error without reporting success.
Exit status `0` indicates success, `1` indicates a file or processing
error, and `2` indicates an incorrect argument count.

This script requires Bash and the standard command-line tools
`basename`, `mkdir` and `tr`.

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

The validation rules and exact output formats are defined in
`data/silwood_trees_metadata.md`.

The workflow is:
`load_records()` → `process_records()` → `summarise_oaks()` → `write_csv()`.

`process_records()` calls `validate_record()` for each source record
and separates accepted records from rejected-row reports.
Only the returned cleaned records are passed to `summarise_oaks()`;
rejected records do not contribute to the oak counts.
`main()` connects these stages and writes the three output tables.

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
logic does not use it; `process_records()` uses the row number
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


### Additional classroom exercises: Shell

#### variables.sh

Demonstrates Bash positional parameters, variable assignment, interactive
input and integer addition. Requires Bash and the external command `expr`.

Run from the project root:

```bash
bash code/variables.sh
bash code/variables.sh 1 "two words"
```

At each run, enter a string, then two integers separated by spaces.
The script prints the arguments, updated string and sum to the terminal.
It does not read or create files.

This teaching example assumes valid integer input; it does not validate
arbitrary input.

#### MyExampleScript.sh

Demonstrates shell variable assignment and expansion by printing
a greeting using `$USER`.

Run from the repository root:

```bash
bash code/MyExampleScript.sh
```

Requires Bash. No input files or command-line arguments are needed.
The script reads `$USER` from the environment and prints the greeting
to the terminal. No output files are created.

#### boilerplate.sh

Provides a minimal Bash script template with a shebang,
documentation comments, a demonstration command and an exit status.

Run from the repository root:

```bash
bash code/boilerplate.sh
```

Alternatively, grant executable permission and run the script directly:

```bash
chmod u+x code/boilerplate.sh
./code/boilerplate.sh
```

Requires Bash. No input files or command-line arguments are needed.
The script prints a demonstration message with surrounding blank lines
to the terminal and creates no output files.

#### CheckLabel.sh

Demonstrates conditional control flow and command-line argument validation.
Requires Bash and exactly one argument: `oak` or `pine`.
No input files are needed.

Run from the repository root:

```bash
bash code/CheckLabel.sh oak
```

A valid label is printed to standard output. An incorrect argument count
produces a usage message on standard error and exit status `2`.
An unknown label produces an error message on standard error and
exit status `1`. Successful execution returns `0`.
No output files are created.


## Testing

### Assignment 1

#### Changes after formative feedback: FASTA commands

The formative feedback confirmed that all five FASTA answers were
correct, so I retained the commands, including `xargs printf '%s'`
for joining the supplied sequence lines.

I clarified the explanations in `unixPrac1.txt`, covering newline
counts, sequence-position counting, motifs spanning line breaks,
and decimal division for the AT/GC ratio. I also expanded the README
instructions and documented the assumptions and limitations of
these methods.

All five commands were rerun from `code/`.
The observed results and checks are recorded in the following section.

#### FASTA command checks

The five commands were rerun from `code/` on 24 November 2026.

| Question | Observed result |
|---|---|
| 1 | Newline counts: 27 for `407228326.fasta`, 127 for `407228412.fasta`, and 78104 for `e_coli.fasta`; total 78258. |
| 2 | Sequence output was inspected and confirmed to exclude the header. |
| 3 | Sequence length: 4686137 positions. |
| 4 | `ATGC` occurrences: 21968. |
| 5 | `(A+T)/(G+C)`: 0.96922822848944879586. |

The two numbered FASTA files lack a final newline, so their newline
counts are one lower than their displayed line counts. The decimal
result printed by `bc` omits the leading zero; this does not change
its value.

#### Delimiter converter checks

##### tabtocsv.sh: changes after formative feedback

The feedback identified that the script assumed a `code/` starting
directory. I changed both the output path and the directory-creation
command from `../results` to `results`, allowing the script to run
from the repository root. I updated the README invocation accordingly.

I retained the existing argument validation, quoted paths, empty-field
preservation and overwrite behaviour.

##### tabtocsv.sh: verification

The revised script was checked on 25 November 2026 from the
repository root.

```bash
bash -n code/tabtocsv.sh
bash code/tabtocsv.sh data/tab-example.tsv
```

Both commands returned status `0`. The generated file,
`results/tab-example.tsv.csv`, contained:

```text
species,count,height
oak,,12
pine,7,16
```

| Check | Observed result |
|---|---|
| Repeated run | Returned status `0`; `diff` confirmed identical output with no appended rows. |
| Input protection | `diff` confirmed that the input remained unchanged after the rerun. |
| Input path containing spaces | Returned status `0`; output matched the normal-path result. |
| Missing argument | Returned status `2` with an error message. |
| Extra argument | Returned status `2` with an error message. |
| Nonexistent input | Returned status `1` with an error message. |
| Directory supplied as input | Returned status `1` with an error message. |
| Unreadable input | Returned status `1` with an error message. |
| Missing results directory | In a separate temporary directory, confirmed that `results/` was absent before execution; the script created it, returned status `0` and generated the expected CSV. |

Exit statuses were inspected immediately after the relevant commands.
All rejected input cases reported an error without displaying `Done!`.

Verification of the revised version in a fresh Git checkout is pending.
The temporary-directory check above tested directory creation, but was
not a Git checkout test.

##### csvtospace.sh: changes after formative feedback

The feedback identified that the script assumed a `code/` starting
directory. I changed both the output path and directory-creation
command from `../results` to `results`, allowing execution from the
repository root. I updated the README invocation accordingly.

I retained the existing argument validation, quoted paths,
empty-field preservation and overwrite behaviour.

##### csvtospace.sh: verification

The revised script was checked on 25 November 2026 from the
repository root.

```bash
bash -n code/csvtospace.sh
bash code/csvtospace.sh data/temperatures/1800.csv
```

Both commands returned status `0`.

| Check | Observed result |
|---|---|
| Four supplied temperature files | All conversions returned status `0`; input and output line counts matched at `1825`, `1825`, `2190` and `1825`, respectively. |
| Repeated runs | All returned status `0`; `diff` confirmed identical outputs without appended rows. |
| Input protection | File comparisons confirmed that all four supplied inputs remained unchanged during these checks. |
| Empty field and spaced input path | A constructed CSV named `field notes.csv` converted successfully; `diff` matched an independently written expected output, including two spaces for the empty field in `oak,,12`. |
| Missing or extra arguments | Returned status `2` with error messages. |
| Nonexistent file, directory input and unreadable file | Returned status `1` with error messages. |
| Missing results directory | In a separate temporary directory, confirmed that `results/` was absent; the script created it, returned status `0` and produced output matching the expected file. |

Exit statuses were inspected immediately after the relevant commands.
Rejected inputs produced error messages without displaying `Done!`.


### Assignment 2

#### Changes after formative feedback

I retained the existing loading, validation, processing, summarising
and writing stages. I clarified the cleaner's documentation of the
retained `source_row` parameter, CSV row numbering, the rule that
rejected records do not reserve identifiers, and the need to reject
non-finite measurements after numeric conversion.

The existing tests were already numbered and labelled by behaviour.
I reviewed their coverage against the metadata and retained that
organisation.

I extended Test 10 to pass the cleaned records returned by
`process_records()` directly to `summarise_oaks()`. The four constructed
input records include two accepted oak records and two rejected oak
records. The resulting summary must contain exactly two `robur`
records, demonstrating that rejected records do not contribute.

I also added checks that processing leaves the input records unchanged
and that an empty input returns two empty lists.

#### Verification

Run the tests and cleaner from the repository root:

```bash
python3 code/test_silwood_trees.py
python3 code/clean_silwood_trees.py
```

All 12 labelled test sections passed, including
the additional assertions in Test 10. The test command and cleaner
both returned exit status `0`.

The tests cover text cleaning, missing and unrecognised values,
permitted and invalid taxon pairs, non-numeric and non-finite
measurements, numeric boundaries, duplicate identifiers, ordered
rejection reasons, record processing and oak summaries.

One useful check rejects `nan`, `inf` and `-inf`: successful conversion
with `float()` does not establish that a measurement is valid.
The processing-to-summary check would detect rejected oak records
being included in the summary.

| Check | Observed result |
|---|---|
| Supplied survey | 36 input records produced 24 accepted records and 12 rejected-row reports. |
| Cleaned table | Accepted identifiers were `ST001`–`ST024` in sorted order; text was canonicalised and numeric values were preserved. |
| Issue table | Source-row numbers, rejection reasons and reason order matched the metadata. |
| Oak summary | `petraea` and `robur` each had count `4`, in species order. |
| Repeated run | All three generated files were identical to their first-run copies according to `diff`. |
| Input protection | The raw CSV and metadata matched copies taken before running the cleaner. |
| Import behaviour | In a separate temporary copy without input data, importing the module returned status `0`, printed no report and created no `results/` directory. |
| Missing results directory | After supplying the raw CSV to that temporary copy, the cleaner created `results/` and returned status `0`. |
| Independent temporary copy | All three generated tables matched the working-copy outputs according to `diff`. |

These checks used the current local files. Verification in a newly
cloned Git repository, following the README commands exactly, is pending.

### Assignment 3

All analyses were run independently from the project root and rerun
successfully.

#### TreeHeight.R: changes after formative feedback

I retained the existing tree-height calculation and input validation.
Following formative feedback, I documented an independent calculation
using a real input record and checked the fixed-input script separately
with normal, boundary and invalid inputs.

#### TreeHeight.R: verification

Both commands below returned exit status `0` when run from the project root:

```bash
Rscript code/TreeHeight.R
Rscript -e 'source("code/TreeHeight.R")'
```

The output contained 120 records and exactly four columns:
`Species`, `Distance.m`, `Angle.degrees` and `height_m`.
A comparison confirmed that all three original columns retained their
input values and row order.

For an independent check, I used the first input record, Populus tremula:

- Horizontal distance: 31.6658337740228 m.
- Angle measured from horizontal: 41.2826361937914 degrees.
- Degrees were converted to radians by multiplying by `pi / 180`.

Without calling `TreeHeight()`, I calculated:

```text
height = 31.6658337740228 × tan(41.2826361937914 × pi / 180)
       ≈ 27.8021161438536 m
```

This matched the first height in `results/TreeHts.csv` within an absolute
tolerance of `1e-10`.

| Check | Observed result |
| --- | --- |
| Repeated run | Returned `0`; `diff` confirmed an identical output. |
| Input protection | `diff` confirmed that the input remained unchanged during the repeated-run check. |
| Missing results directory | A temporary project created `results/` automatically and produced an identical CSV. |
| Distance 0 or 101 | Returned `1` with a distance-range error and created no output. |
| Angle 0 or 90 | Returned `1` with an angle-range error and created no output. |
| Text in either measurement column | Returned `1` with a numeric-type error and created no output. |
| Infinite distance or NaN angle | Returned `1` with a finite-value error and created no output. |
| Missing distance or angle | Returned `1` with a numeric-type error and created no output. |
| Missing or extra column | Returned `1` with a column-validation error and created no output. |
| Distance 100 m and angle 45 degrees | Returned `0` and produced a height of 100 m. |

Invalid-input and directory-creation checks used isolated temporary
projects without modifying the supplied input file.

#### get_TreeHeight.R: changes after formative feedback

I retained the existing calculation and input-validation logic.
Following formative feedback, I checked the generalised route separately
and documented an independent height comparison against both programs'
outputs.

#### get_TreeHeight.R: verification

The following command completed with exit status `0` from the project root:

```bash
Rscript code/get_TreeHeight.R data/trees.csv
```

The output contained 120 records with the required four columns.
All original columns retained their input values and row order.
The fixed and generalised output tables also matched.

For the first record, Populus tremula, the independent calculation
documented above gave approximately 27.8021161438536 m.
Both `results/TreeHts.csv` and `results/trees_treeheights.csv` matched
this value within an absolute tolerance of `1e-10`.

| Check | Observed result |
| --- | --- |
| Repeated run | Returned `0`; `diff` confirmed identical output and unchanged input during the check. |
| Spaced input path and output naming | `data/tree measurements.csv` produced `results/tree measurements_treeheights.csv`, matching the verified output. |
| Missing results directory | The script created `results/` automatically in a temporary project. |
| Missing or extra arguments | Returned `1` with an argument-count error. |
| Missing file, directory input or unreadable file | Returned `1` with an appropriate error; these checks created no results directory. |
| Distance 0 or 101; angle 0 or 90 | Returned `1` with range errors and created no output. |
| Text or missing values in either measurement column | Returned `1` with numeric-type errors and created no output. |
| Infinite distance or NaN angle | Returned `1` with finite-value errors and created no output. |
| Missing or extra column | Returned `1` with a column-validation error and created no output. |
| Distance 100 m and angle 45 degrees | Returned `0` and produced a height of 100 m. |

Invalid-input checks used isolated temporary projects.

For interactive debugging, I temporarily placed `browser()` immediately
before the height calculation, started R using
`R --vanilla --args data/trees.csv`, and sourced the script.
I inspected the first record and calculated its expected height.
The subsequent height comparison passed with a tolerance of `1e-10`.

I removed the temporary breakpoint and reran the normal command.
It completed without an interactive pause and returned exit status `0`.

#### run_get_TreeHeight.sh: verification

The wrapper was retained because its invocation and failure handling
already matched the requirements. Its behaviour was checked separately
after reviewing the R scripts.

Run from the project root:

```bash
bash code/run_get_TreeHeight.sh
```

| Check | Observed result |
| --- | --- |
| Syntax | `bash -n code/run_get_TreeHeight.sh` returned `0`. |
| Normal execution | The wrapper returned `0`; `diff` confirmed that its output matched the previously verified CSV. |
| Failure propagation | In a temporary project containing both scripts but no input data, the R script reported the missing file and the wrapper returned `1`. No results directory was created. |

#### pound_hill_analysis.R: changes after formative feedback

I retained the quadrat-to-plot richness calculation and figure.
Following formative feedback, I documented a check tracing one plot
from the raw species counts through quadrat richness and the plot mean
to the saved CSV and figure.

I clarified the metadata-based reason for treating blank species counts
as observed zeros. I also added a finite-value check while retaining
the missing-value and negative-count checks.

#### pound_hill_analysis.R: verification

Run from the project root:

```bash
Rscript code/pound_hill_analysis.R
```

The analysis returned exit status `0` and identified 41 species,
59 quadrats and 12 plots. The saved richness table contained one row
per plot.

For an independent check, I selected Plot 12 under May cultivation,
Block d, directly from the raw wide-format data.

| Recorded quadrat | Independently calculated richness |
| --- | ---: |
| Q1 | 9 |
| Q2 | 8 |
| Q4 | 10 |

The mean was `(9 + 8 + 10) / 3 = 9`, matching `MeanRichness` in
`results/pound_hill_plot_richness.csv` within a tolerance of `1e-10`.
Q3 was not recorded and was not added as a zero-valued quadrat.

The PDF was opened and inspected. The May point at richness 9,
coloured for Block d, matched Plot 12. Axes and the block legend were
readable, and the plotted points matched the saved table.

The interpretation describes mean species richness rather than
abundance, acknowledges overlapping observed ranges among treatments,
and avoids inferring causation from the figure alone.

| Check | Observed result |
| --- | --- |
| Repeated execution | Returned `0`; `diff` confirmed an identical richness CSV. |
| Input protection | Comparisons confirmed that the data and metadata remained unchanged during the checks. |
| PDF regeneration | The rerun produced a nonempty PDF. |
| Missing results directory | A temporary project created both nonempty outputs and produced a richness CSV identical to the verified result. |
| Negative count (`-1`) | Returned `1` with a negative-count error; neither output was created. |
| Text count (`many`) | Returned `1` after conversion produced a missing value; neither output was created. |
| Infinite count (`Inf`) | Returned `1` with a finite-value error; neither output was created. |

Invalid-input checks modified only temporary copies of the data.

### Additional classroom exercises: Shell

#### variables.sh

- `bash -n code/variables.sh` returned status `0`.
- Runs with no arguments and with `1 "two words"` showed the expected
  argument counts and values.
- Interactive string input updated the displayed variable.
- Integer inputs `3 5` and `-3 0` produced `8` and `-3`.
- Bash arithmetic expansion was temporarily substituted for `expr`
  and also produced `8` for `3 5`; the final script retains `expr`.

#### MyExampleScript.sh

The script was run from the repository root.
It printed `Hello` followed by the value of `$USER`, as expected.

#### boilerplate.sh

Both `bash code/boilerplate.sh` and direct
execution using `./code/boilerplate.sh` were checked from the
repository root, after granting executable permission with `chmod u+x`.
Both printed `This is a shell script!` with surrounding blank lines,
as expected.

#### CheckLabel.sh

The following checks were run from the
repository root. Exit statuses were inspected immediately after
each invocation using `echo "$?"`.

| Arguments | Observed result | Exit status |
| --- | --- | --- |
| `oak` | Printed the selected label. | `0` |
| None | Printed the usage message. | `2` |
| `birch` | Reported an unknown label. | `1` |
| `oak pine` | Printed the usage message. | `2` |

All four checks matched the expected behaviour.


## Limitations

### Assignment 1
- FASTA commands assume the supplied single-record files and uppercase sequence letters. `wc -l` counts newlines; the two numbered FASTA files lack a final newline.
- Ambiguous bases are included in sequence length but excluded from the AT/GC ratio.
- Questions 3 and 4 use `xargs printf '%s'` to join the supplied
  sequence-only lines. This is suitable for these inputs, but is not
  a general text-preserving method because `xargs` interprets
  whitespace, quotes and backslashes. For the supplied ASCII sequence
  symbols, the resulting byte count equals the number of sequence
  positions.
- Ambiguous nucleotide symbols are retained during motif searching.
  The motif `ATGC` cannot overlap with itself, so non-overlapping
  matching counts all its occurrences. The AT/GC ratio is undefined
  if the G+C count is zero; the supplied sequence has a nonzero count.
- The converters replace characters rather than fully parsing CSV/TSV. Quoted delimiters and spaces within fields may produce ambiguous output.
- Input and output must be independent files; links between them are not checked. Existing output is overwritten.

### Assignment 2

- Source-row numbering assumes one record per line, with no blank lines between records.
- Each input record must contain all six fields as strings. Empty cells are handled, but structurally missing fields that CSV reading represents as `None` are not supported.
- The cleaner supports only the column layout, locations and taxon pairs specified in the supplied metadata.

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