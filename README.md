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
│   ├── assignment-2-2026.md
│   └── assignment-3-2026.md
├── code/
│   ├── CheckLabel.sh
│   ├── ConcatenateTwoFiles.sh
│   ├── CountLines.sh
│   ├── MyExampleScript.py
│   ├── MyExampleScript.sh
│   ├── TreeHeight.R
│   ├── basic_io.R
│   ├── boilerplate.R
│   ├── boilerplate.py
│   ├── boilerplate.sh
│   ├── break.R
│   ├── browse.R
│   ├── cfexercises1.py
│   ├── cfexercises2.py
│   ├── clean_silwood_trees.py
│   ├── control_flow.R
│   ├── control_flow.py
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
│   ├── sysargv.py
│   ├── tabtocsv.sh
│   ├── test_control_flow.py
│   ├── test_observations_practice.py
│   ├── test_silwood_trees.py
│   ├── tiff2_png.sh
│   ├── try.R
│   ├── unixPrac1.txt
│   ├── using_name.py
│   └── variables.sh
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
│   ├── bootcamp_observations.csv
│   ├── bootcamp_observations_boundary.csv
│   ├── bootcamp_observations_invalid.csv
│   ├── pound_hill_data.csv
│   ├── pound_hill_meta_data.csv
│   ├── silwood_trees_metadata.md
│   ├── silwood_trees_raw.csv
│   ├── tab-example.tsv
│   └── trees.csv
└── results/
    └── .gitkeep
```

Required scripts and inputs are tracked in Git. Generated results,
the Python virtual environment, caches and R session files are ignored.
Only `.gitkeep` is tracked inside `results/`. Other local practice
and editor files are not part of the submitted repository.

## Requirements

Development checks used Ubuntu 26.04.1 LTS, Bash 5.3.9,
Git 2.53.0, Python 3.14.4 and R 4.5.2.
Fresh-clone Python checks were also run after deactivating the
development virtual environment.

Python scripts use the standard library.
Shell exercises use Bash and standard command-line tools;
the FASTA ratio calculation additionally requires `bc`.

The tidy R script requires R 4.1 or later for the native pipe.
Additional R packages are:

| Scripts | Packages |
| --- | --- |
| `pound_hill_analysis.R` | `reshape2`, `dplyr`, `ggplot2` |
| `data_wrang.R` | `reshape2` |
| `data_wrang_tidy.R` | `dplyr`, `tidyr` |

Other documented R scripts use base R.

Install missing R packages once from an R session:

```r
install.packages(c("reshape2", "dplyr", "tidyr", "ggplot2"))
```

`tiff2_png.sh` requires ImageMagick's `convert` command.
Conversion checks used ImageMagick 7.1.2-18.

## Data

All required input files are included in `data/`; no additional
download is needed for the documented CSV and FASTA workflows.
Supplied source files are retained unchanged. Derived tables and
figures are written separately to `results/`.

| Input path, relative to data/ | Contents and use |
| --- | --- |
| `fasta/407228326.fasta` | Supplied sequence used for the FASTA inspection and newline-count exercise. |
| `fasta/407228412.fasta` | Supplied sequence used for the FASTA inspection and newline-count exercise. |
| `fasta/e_coli.fasta` | Supplied E. coli sequence used for header removal, sequence length, motif counting and the AT/GC ratio. |
| `temperatures/1800.csv` | Supplied input for comma-to-space conversion. |
| `temperatures/1801.csv` | Supplied input for comma-to-space conversion. |
| `temperatures/1802.csv` | Supplied input for comma-to-space conversion. |
| `temperatures/1803.csv` | Supplied input for comma-to-space conversion. |
| `tab-example.tsv` | Small test input containing an empty field, used for tab-to-comma conversion and line counting. |
| `silwood_trees_raw.csv` | Synthetic tree-survey records processed by the Assignment 2 cleaner. |
| `silwood_trees_metadata.md` | Defines the tree-survey fields, validation rules and required outputs. |
| `trees.csv` | Supplied 120-record table containing Species, Distance.m and Angle.degrees; used for tree-height calculation and the basic R file-I/O exercise. |
| `pound_hill_data.csv` | Plant species counts and sampling-design labels used by both wrangling scripts and the richness/abundance analysis. |
| `pound_hill_meta_data.csv` | Semicolon-delimited metadata describing the Pound Hill fields and the meaning of blank species counts. |
| `bootcamp_observations.csv` | Ordinary observations containing known counts, a missing count and an exact duplicate; used by the Python and R observations exercises. |
| `bootcamp_observations_boundary.csv` | Boundary observations distinguishing an all-missing site from an observed-zero site, including a duplicate zero record. |
| `bootcamp_observations_invalid.csv` | Deliberately invalid counts, -1 and many, used for validation checks. |


The supplied exercise datasets are from the
[MulQuaBio course materials](https://mulquabio.github.io/MQB/).

Blank Pound Hill species counts represent observed absences and
are converted to zero according to its metadata. Blank counts in
the observations exercise instead represent missing observations.
These dataset-specific rules must not be interchanged.

Additional synthetic test cases are defined in test scripts or
created using the documented temporary-file commands. They are
not additional source datasets.

The TIFF conversion demonstration requires expendable TIFF inputs
supplied by the user; no TIFF fixture is included in this repository.


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

#### CountLines.sh

Counts newline characters in one readable regular file.
Requires Bash and `wc`.

Run from the repository root, supplying an input file path:

```bash
bash code/CountLines.sh data/tab-example.tsv
```

Quote paths containing spaces. The script prints the filename and
newline count to the terminal, followed by a blank line.
It creates no output files.

An unterminated final line is not counted.
Exit status `0` indicates success, `2` indicates an incorrect
argument count, and `1` indicates an invalid input or counting failure.
Errors are reported on standard error.

#### ConcatenateTwoFiles.sh

Combines two readable regular files in argument order.
Requires Bash and `cat`.

The script takes two input paths and one output path.
For a reproducible example, first create the temporary inputs
described in Testing, then run from the repository root:

```bash
bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/combined.txt
```

Replace the example paths with your own files and quote paths containing
spaces. The output must be separate from both inputs and must not be
an existing file you need to preserve.

The script writes the first input using `>`, then appends the second
using `>>`. Rerunning replaces the previous output. It prints a heading
and the combined contents to the terminal. Input files are not modified
when the output refers to a separate file.

Exit status `0` indicates success, `2` indicates an incorrect argument
count, and `1` indicates a validation or write failure.
A failure while displaying the output returns the final `cat` command's
nonzero status. Errors are reported on standard error.

Files are concatenated without inserting a separator or newline.
If the first input lacks a final newline, the second input begins
immediately after its last character.

#### tiff2_png.sh

Demonstrates a shell loop that converts lowercase `.tif` files to PNG.
Requires Bash, `basename` and ImageMagick's `convert` command.
It takes no command-line arguments.

The script processes the current working directory and writes PNG files
there using the same filename stems. Existing PNG outputs may be overwritten.

From the repository root, save the script path and prepare a test directory:

```bash
project_root=$PWD
script_path="$project_root/code/tiff2_png.sh"
mkdir -p sandbox/tiff_checks
cd sandbox/tiff_checks
```

Copy expendable TIFF images into this directory. Use lowercase `.tif`
extensions, filenames not beginning with `-`, and no existing PNG outputs.

Check the converter and preview input/output names before running:

```bash
command -v convert

for filename in *.tif
do
    printf 'Input: <%s> Output: <%s>\n' \
        "$filename" "$(basename "$filename" .tif).png"
done
```

If `convert` is unavailable or the preview shows literal `*.tif`,
do not run the conversion. Otherwise, run:

```bash
bash "$script_path"
```

Return to the repository root afterwards:

```bash
cd "$project_root"
```

### Additional classroom exercises: Python

#### MyExampleScript.py

Demonstrates defining and calling a function, returning a value,
and displaying the result with an f-string.

Requires Python 3 and no additional packages.
Run from the repository root:

```bash
python3 code/MyExampleScript.py
```

No input files or command-line arguments are needed.
The script prints `The square of 2 is 4` and creates no output files.
The demonstration runs at module level, so importing the module
also prints the result.

#### boilerplate.py

Demonstrates a main function and main guard, separating reusable
definitions from program startup.

Requires Python 3 and no additional packages.
Run from the repository root:

```bash
python3 code/boilerplate.py
```

No input files or command-line arguments are needed.
Direct execution prints `This is a boilerplate`.
Importing the module does not run `main()` automatically.
No output files are created.

#### using_name.py

Demonstrates how Python assigns `__name__` during direct execution
and import. Requires Python 3 and no additional packages.

Run from the repository root:

```bash
python3 code/using_name.py
```

Direct execution prints `This module's name is: __main__`.
Importing the module produces no message; `module_name()` then
returns `using_name`.

No input files or command-line arguments are needed.
No output files are created.

#### sysargv.py

Demonstrates reading command-line arguments with `sys.argv`.
Requires Python 3 and uses only the standard library.

Run from the repository root:

```bash
python3 code/sysargv.py
python3 code/sysargv.py oak 12
```

The script prints its invocation path, the number of user-supplied
arguments and their list. Arguments are strings, including values
such as `12`. Quote arguments containing spaces.

No arguments are required. No input files are read and no output
files are created.

#### loops.py

Demonstrates iteration over a range and a mixed-type list,
cumulative addition, and a while loop.

Requires Python 3 and no additional packages.
Run from the repository root:

```bash
python3 code/loops.py
```

No input files or command-line arguments are needed.
The script prints four sequences to the terminal and creates no
output files. The examples execute at module level.

#### cfexercises1.py

Demonstrates square roots, comparisons, three-value sorting,
and factorial calculation using a for loop, recursion and a while loop.

Requires Python 3 and no additional packages.
Run from the repository root:

```bash
python3 code/cfexercises1.py
```

The script prints representative function results, including comparisons
of the three factorial methods for `0`, `1` and `5`.
Importing the module does not run these examples.

No input files or command-line arguments are needed.
No output files are created.

Functions assume non-negative real inputs for square roots,
comparable real numbers for comparisons, and small non-negative
integers for factorials. Invalid inputs are not explicitly checked.
The recursive implementation is subject to Python's recursion limit.

#### cfexercises2.py

Demonstrates for and while loops, remainder conditions, if/elif,
nested loops and break.

Requires Python 3 and no additional packages.
Run from the repository root:

```bash
python3 code/cfexercises2.py
```

The script runs six examples, printing greetings and a space-only
separator line after each example. Importing the module does not
run the examples.

No input files or command-line arguments are needed.
No output files are created.

Inputs are assumed to satisfy the documented conditions.
For integer inputs, `hello_4(x)` terminates only when `x <= 15`
and `15 - x` is divisible by three. When `x` is True,
`hello_6(x, y)` requires an integer starting value `y < 6`
to reach its break condition. Invalid inputs are not explicitly checked.

#### control_flow.py

Defines reusable functions for parity, divisors, prime numbers and
counting heights strictly above a threshold. A guarded main function
prints representative results.

Requires Python 3 and no additional packages.
Run from the repository root:

```bash
python3 code/control_flow.py
```

No input files or command-line arguments are needed.
No output files are created. Importing the module does not run
the demonstration.

#### test_control_flow.py

Imports and checks the five functions in `control_flow.py` using
assertions and an expected-exception check. It does not duplicate
the function implementations.

Run from the repository root:

```bash
python3 code/test_control_flow.py
```

Requires Python 3 and `control_flow.py` alongside it in `code/`.
No input files or command-line arguments are needed.
Successful execution produces no output and returns exit status `0`.
Do not use Python's `-O` option, which disables assertions.
No output files are created.

#### observations_practice.py

Loads CSV observations, converts count text and summarises records
by site. Requires Python 3 and the standard-library `csv` module.

Run from the repository root:

```bash
python3 code/observations_practice.py
```

The report reads `data/bootcamp_observations.csv` and prints each
distinct site's known-count total and missing-count number in
sorted site order. No command-line arguments are needed and no
output files are created.

Each row must contain exactly the text fields `site`, `date` and
`count`. Site and date must be non-empty. Blank counts represent
missing observations; other counts must convert to non-negative
integers. Every row is validated, including rows for other sites.

Exact duplicate `(site, date, count)` records are counted once.
Known zero counts remain distinct from missing values.
A site with no known count has total `None`.
Input rows are not modified.

The module also retains `suggested_total`, a deliberately faulty
textbook example used only for critique. The report uses
`summarise_site`, not this faulty example.

#### test_observations_practice.py

Imports and tests the observation functions without copying their
implementations. Requires Python 3, the implementation module and:

- `data/bootcamp_observations.csv`
- `data/bootcamp_observations_boundary.csv`
- `data/bootcamp_observations_invalid.csv`

Run from the repository root:

```bash
python3 code/test_observations_practice.py
```

Successful execution produces no output and returns exit status `0`.
No output files are created.

#### debugme.py

Demonstrates investigating and handling division by zero.
Requires Python 3 and no additional packages.

Run from the repository root:

```bash
python3 code/debugme.py
```

The guarded demonstration calls `buggyfunc(20)`, prints successful
divisions and a division-by-zero message, then displays the last
successful result, `20.0`.

No input files or command-line arguments are needed.
No output files are created. The final version has no active breakpoint.

### Additional classroom exercises: R

#### basic_io.R

Demonstrates reading data and writing, appending and overwriting files
using base R. No command-line arguments or additional packages are required.

- Input: `data/trees.csv`, with a header row.
- Output: `results/MyData.csv`; the script creates `results/` if needed.
- Run all commands from the repository root.

From the shell:

```bash
Rscript code/basic_io.R
```

Alternatively, start a clean R session with `R --vanilla`, then enter:

```r
source("code/basic_io.R")
q(save = "no")
```

The append step produces the expected warning
`appending column names to file`. Later writes overwrite that intermediate
content. The final file includes row names and omits column names;
it is space-separated despite its `.csv` filename.


#### boilerplate.R

Demonstrates a function taking two arguments, printing their values
and classes, and returning their combined vector.

Requires base R only. No input files, command-line arguments or
output files are used.

Run from the repository root:

```bash
Rscript code/boilerplate.R
```

Alternatively, start R with `R --vanilla`, then enter:

```r
source("code/boilerplate.R")
MyFunction(1, 2)
MyFunction("riki", "Tiki")
q(save = "no")
```
#### control_flow.R

Demonstrates conditional statements, numeric and character `for` loops,
and a terminating `while` loop.

Requires base R only. No command-line arguments, input files or output
files are used.

Run from the repository root:

```bash
Rscript code/control_flow.R
```

Alternatively, start R with `R --vanilla` from the repository root,
then enter:

```r
source("code/control_flow.R")
q(save = "no")
```

The random conditional message appears only when the generated value
is at most 0.5, so its presence may differ between runs.

#### r_conditionals.R

Defines functions that return messages describing integer parity,
powers of 2 and primality.

Requires base R only. No command-line arguments, input files or
output files are used. Function inputs are assumed to be single
finite integers.

Run from the repository root:

```bash
Rscript code/r_conditionals.R
```

Alternatively, start R with `R --vanilla` from the repository root,
then enter:

```r
source("code/r_conditionals.R")
q(save = "no")
```

Both methods print the three demonstration results. Sourcing also
makes `is.even`, `is.power2` and `is.prime` available for further calls.
The power-of-2 check includes 1, since `1 = 2^0`.

#### break.R

Demonstrates using `break` to exit a `while` loop when the counter
reaches 10, printing values from 0 to 9.

Requires base R only. No command-line arguments, input files or
output files are used.

Run from the repository root:

```bash
Rscript code/break.R
```

Alternatively, start R with `R --vanilla` from the repository root,
then enter:

```r
source("code/break.R")
q(save = "no")
```
#### next.R

Demonstrates using `next` to skip even numbers in a loop over 1–10,
printing only 1, 3, 5, 7 and 9.

Requires base R only. No command-line arguments, input files or
output files are used.

Run from the repository root:

```bash
Rscript code/next.R
```

Alternatively, start R with `R --vanilla` from the repository root,
then enter:

```r
source("code/next.R")
q(save = "no")
```

#### try.R

Demonstrates catching sampling errors with `try()` using both
`lapply()` and a preallocated list with a `for` loop.

Requires base R only. No command-line arguments or input files are
needed. The script creates `results/` if necessary and saves a
population histogram to `results/try_population.pdf`.

Run from the repository root:

```bash
Rscript code/try.R
```

Alternatively, start R with `R --vanilla` from the repository root,
then enter:

```r
source("code/try.R")
q(save = "no")
```

The script uses `set.seed(1345)`. Each method attempts 15 samples,
printing means when more than 30 distinct values are sampled.
Errors remain visible but are caught, allowing subsequent attempts
to continue. Each result list is printed; the second replaces
`result` from the first. Successful entries contain text messages,
while failed entries have class `"try-error"`.

Rerunning replaces the histogram PDF.

#### browse.R

Demonstrates interactive debugging with `browser()` during an
exponential-growth simulation.

Requires base R only. No command-line arguments or input files are
needed. The example assumes `generations` is an integer of at least 2.

From the repository root, start an interactive R session:

```bash
R --vanilla
```

At the R prompt, enter:

```r
source("code/browse.R")
```

At each `Browse[...]` prompt, inspect variables using `ls()`, `t`
and `N`. Use `n` to step or `c` to continue. The breakpoint is inside
the loop, so continuing pauses again on subsequent iterations.

After continuing through all iterations, the script saves
`results/browse_exponential.pdf` and closes the PDF device.
The directory is created if needed; rerunning replaces the PDF.

To abort debugging, enter uppercase `Q`. Because the PDF device
opens before the simulation, an aborted run requires `dev.off()`
at the ordinary R prompt to close it. That run may leave an
incomplete PDF.

Exit R with `q(save = "no")`. This exercise is intended for
interactive sourcing.

#### observations_practice.R

Reads, validates and summarises ecological observations using functions,
loops, missing-value handling, assertions and base-R plotting.

Requires base R only. Run from the repository root:

```bash
Rscript code/observations_practice.R
```

No command-line arguments are required. The script reads:

| Input | Purpose |
| --- | --- |
| `data/bootcamp_observations.csv` | Ordinary observations, including a duplicate and a missing count. |
| `data/bootcamp_observations_boundary.csv` | All-missing counts and duplicated observed zeros. |
| `data/bootcamp_observations_invalid.csv` | Invalid counts for error-handling checks. |

Each CSV must contain exactly the columns `site,date,count` in that
order. Site and date must be non-empty. Blank counts represent missing
observations; other counts must be non-negative integers within R's
integer range.

`read_observations()` reads fields as text, validates them and converts
counts to integers. `summarise_observations()` removes exact duplicate
rows and calculates each site's known-count total and missing-count
number, retaining site order of first occurrence.

Known zeros remain distinct from missing values. A site with only
missing counts has total `NA`.

The script prints the ordinary data, both summary tables and the
expected invalid-input error caught by `try()`. Embedded assertions
check the four site summaries and confirm that the invalid file
raises an error.

The script creates `results/` if needed and writes
`results/observations_known_totals.pdf`, replacing the PDF on reruns.
No summary CSV is written.

#### data_wrang.R

Reshapes the Pound Hill dataset from wide to long format using
`reshape2::melt()`.

Requires `reshape2`; see Requirements for installation.

Run from the repository root:

```bash
Rscript code/data_wrang.R
```

No command-line arguments are required. Inputs are:

- `data/pound_hill_data.csv`, read without a header.
- `data/pound_hill_meta_data.csv`, read with a header and semicolon separators.

The script inspects and transposes the raw table, sets column names
and converts blank species counts to zero, as specified by the metadata.
It reshapes species columns into `Species` and `Count`, retaining
`Cultivation`, `Block`, `Plot` and `Quadrat` as identifiers.

The four identifier columns and `Species` are factors; `Count` is
integer. The script writes `results/pound_hill_long.csv` without row
names, creates `results/` if needed and replaces the CSV on reruns.
The raw files are only read. No figure is generated.

#### data_wrang_tidy.R

Recreates the Pound Hill wide-to-long transformation using
`tidyr::pivot_longer()` and `dplyr::mutate()`.

Requires R 4.1 or later, `dplyr` and `tidyr`;
see Requirements for installation.

Run from the repository root:

```bash
Rscript code/data_wrang_tidy.R
```

No command-line arguments are required. Inputs are:

- `data/pound_hill_data.csv`, read without a header.
- `data/pound_hill_meta_data.csv`, read with a header and semicolon separators.

The script transposes the raw table, assigns column names and converts
blank species counts to zero according to the metadata. It retains
`Cultivation`, `Block`, `Plot` and `Quadrat` as identifiers, and gathers
species columns into `Species` and `Count`.

The five categorical columns are factors; `Count` is integer.
The script creates `results/` if needed and writes
`results/pound_hill_long.csv` without row names. No figure is generated.

This output path is shared with `data_wrang.R`: whichever script runs
last replaces the CSV. Their row order differs, but their records
should match after sorting. The raw input files are only read.

## Testing

### Assignment 1

### Fresh-clone verification

On 27 November 2026, commit 681a5eb was cloned from origin into
a new directory. Checks were run from that clone's repository root,
after deactivating the development Python virtual environment.

| Scope | Result |
| --- | --- |
| Delimiter converters | TSV example and all four temperature files completed successfully. |
| Assignment 2 | Cleaner and independent test script completed successfully. |
| Assignment 3 | Both tree-height scripts, the shell wrapper and Pound Hill analysis completed successfully. |
| Python exercises | Twelve demonstration and test scripts completed successfully. |
| R exercises | Ten non-interactive classroom scripts and the additional basic plotting exercise completed successfully. |
| Shell checks | All tracked Shell scripts passed syntax checks; four selected demonstrations completed successfully. |
| Outputs | All 16 checked result files existed and were nonempty. |
| Input and code protection | `git diff --exit-code HEAD` passed; tracked files were unchanged and the working tree remained clean. |

All batch checks returned exit status 0. These checks establish
execution and output presence; the detailed numerical, boundary,
rerun and visual checks are documented below.

Warning searches matched basic_io.R and observations_practice.R logs.
Their warning details require confirmation against the expected
append-header and incomplete-final-line warnings documented below.

The batch did not repeat the FASTA commands, interactive browse.R
debugging or all Shell input scenarios. Earlier checks remain
documented separately.

TIFF-to-PNG conversion was subsequently tested separately in the
same fresh clone using ImageMagick 7.1.2-18. Both synthetic test
images converted successfully, retaining their dimensions and
showing zero differing pixels. Details are recorded under
`tiff2_png.sh` below.

The verification clone was subsequently updated to commit e2a3b71
using git pull --ff-only. This update removed the additional basic
plotting exercise and its dedicated dataset, and revised the README.
The working tree remained clean. The full test batch was not rerun
after this cleanup.

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

The additional basic plotting exercise and its dedicated input
were subsequently removed following teaching-assistant advice
to retain only the requested coursework scope.


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

Normal execution and syntax were subsequently checked in the fresh clone; the earlier edge-case checks were not repeated there.

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

The cleaner and independent test script were subsequently rerun successfully in the fresh clone. The detailed output comparisons above were performed during the earlier local checks.

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

#### CountLines.sh

The teaching starter was extended with argument-count validation,
readable-file checks and immediate checking of the counting command's
exit status. Comments explain newline counting and failure handling.

The following checks were completed locally.
Temporary test files are not tracked by Git. To reproduce the checks,
run the following commands from the repository root.

Create or reset the disposable test files:

```bash
mkdir -p sandbox/countlines_checks

printf 'oak\npine\n' > sandbox/countlines_checks/two_lines.txt
printf 'oak\npine' > sandbox/countlines_checks/no_final_newline.txt
printf '' > sandbox/countlines_checks/empty.txt
printf 'oak\npine\n' > "sandbox/countlines_checks/field notes.txt"
```

Check syntax, normal input and boundary cases:

```bash
bash -n code/CountLines.sh
echo "$?"

bash code/CountLines.sh sandbox/countlines_checks/two_lines.txt
echo "$?"

bash code/CountLines.sh sandbox/countlines_checks/no_final_newline.txt
echo "$?"

bash code/CountLines.sh sandbox/countlines_checks/empty.txt
echo "$?"

bash code/CountLines.sh "sandbox/countlines_checks/field notes.txt"
echo "$?"
```

Check invalid arguments and input paths. The path `missing.txt`
must not exist:

```bash
bash code/CountLines.sh
echo "$?"

bash code/CountLines.sh sandbox/countlines_checks/two_lines.txt extra
echo "$?"

bash code/CountLines.sh sandbox/countlines_checks/missing.txt
echo "$?"

bash code/CountLines.sh sandbox/countlines_checks
echo "$?"
```

Check an unreadable file, then restore read permission.
Run this check as an ordinary user, not as root:

```bash
printf 'oak\n' > sandbox/countlines_checks/unreadable.txt
chmod ugo-r sandbox/countlines_checks/unreadable.txt

bash code/CountLines.sh sandbox/countlines_checks/unreadable.txt
echo "$?"

chmod u+r sandbox/countlines_checks/unreadable.txt
```

| Check | Observed result | Exit status |
| --- | --- | --- |
| Syntax | No syntax errors reported. | `0` |
| Two newline-terminated lines | Counted `2`. | `0` |
| Two text lines without a final newline | Counted `1`. | `0` |
| Empty file | Counted `0`. | `0` |
| Filename containing spaces | Counted `2`. | `0` |
| Missing argument | Printed a usage message. | `2` |
| Extra argument | Printed a usage message. | `2` |
| Nonexistent file | Reported invalid input. | `1` |
| Directory input | Reported invalid input. | `1` |
| Unreadable file | Reported invalid input. | `1` |

All checks matched the expected behaviour. Exit statuses were inspected
immediately after the relevant commands. Rejected inputs produced
no normal count report. Read permission was restored after testing.

#### ConcatenateTwoFiles.sh

The teaching starter was extended with argument-count validation,
readable-input checks, identical-path rejection and immediate checks
after writing and appending. The original two-step redirection was retained.
Comments explain overwrite behaviour and the checks.

The following checks were completed locally.
Temporary test files are not tracked by Git. To reproduce the checks,
run the following commands from the repository root.

Create or reset the disposable test files:

```bash
mkdir -p sandbox/concatenate_checks

printf 'oak\n' > sandbox/concatenate_checks/first.txt
printf 'pine\n' > "sandbox/concatenate_checks/second file.txt"
printf 'oak\npine\n' > sandbox/concatenate_checks/expected.txt
```

Check syntax, concatenation order and a filename containing spaces:

```bash
bash -n code/ConcatenateTwoFiles.sh
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/combined.txt
echo "$?"

diff sandbox/concatenate_checks/expected.txt sandbox/concatenate_checks/combined.txt
echo "$?"
```

Repeat the execution and comparison to check that rerunning replaces
the output without duplicating its contents:

```bash
bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/combined.txt
echo "$?"

diff sandbox/concatenate_checks/expected.txt sandbox/concatenate_checks/combined.txt
echo "$?"
```

Check invalid arguments and inputs. The path `missing.txt` must not exist:

```bash
bash code/ConcatenateTwoFiles.sh
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/combined.txt extra
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/missing.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/combined.txt
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    sandbox/concatenate_checks/missing.txt \
    sandbox/concatenate_checks/combined.txt
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/combined.txt
echo "$?"
```

Check identical input/output path rejection using only the disposable files:

```bash
bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks/first.txt
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    "sandbox/concatenate_checks/second file.txt"
echo "$?"
```

Check that both inputs are unchanged, then test a directory as the output:

```bash
printf 'oak\n' | diff - sandbox/concatenate_checks/first.txt
echo "$?"

printf 'pine\n' | diff - "sandbox/concatenate_checks/second file.txt"
echo "$?"

bash code/ConcatenateTwoFiles.sh \
    sandbox/concatenate_checks/first.txt \
    "sandbox/concatenate_checks/second file.txt" \
    sandbox/concatenate_checks
echo "$?"
```

| Check | Observed result |
| --- | --- |
| Syntax | Returned `0`. |
| Normal execution with a spaced input path | Printed `oak` followed by `pine` and returned `0`; `diff` returned `0`. |
| Repeated run | Returned `0`; `diff` confirmed no duplicated content. |
| Missing or extra arguments | Printed usage messages and returned `2`. |
| Either input nonexistent | Reported invalid input and returned `1`. |
| Directory as input | Reported invalid input and returned `1`. |
| Output path identical to either input path | Rejected the operation and returned `1`. |
| Input protection | Both comparisons returned `0`, confirming unchanged input contents. |
| Directory as output | Reported a write failure and returned `1`, without printing the merge heading. |

All checks matched the expected behaviour. Exit statuses were inspected
immediately after the relevant commands. A successful `diff` printed
nothing and returned `0`.

These checks do not verify detection of different paths referring
to the same file; see Limitations.

#### tiff2_png.sh

Actual conversion was subsequently checked in the fresh clone on
27 November 2026 using ImageMagick 7.1.2-18.

Two synthetic TIFF images were created in a temporary directory:
red.tif (100 × 60 pixels) and blue sample.tif (80 × 50 pixels).
Both converted successfully, including the filename containing a space.
The script returned exit status 0.

identify confirmed PNG output with unchanged dimensions.
compare -metric AE reported zero differing pixels for both pairs,
with comparison exit status 0. These checks cover the two synthetic
solid-colour fixtures, not arbitrary TIFF formats or metadata preservation.

Test files remained outside the repository, and the working tree
was clean afterwards.

### Additional classroom exercises: Python

#### MyExampleScript.py

Running `python3 code/MyExampleScript.py` from the repository root
printed `The square of 2 is 4`, matching the independent calculation
`2 * 2 = 4`. The exit status was inspected immediately afterwards
using `echo "$?"` and was `0`.

#### boilerplate.py

Direct execution from the repository root printed
`This is a boilerplate`. The exit status was inspected immediately
using `echo "$?"` and was `0`.

Import behaviour was also checked in a fresh Python session started
from the repository root:

```bash
python3
```

At the Python prompt, enter each statement separately:

```python
import sys
sys.path.insert(0, "code")
import boilerplate
boilerplate.main()
exit()
```

Importing the module produced no message. Explicitly calling
`boilerplate.main()` printed `This is a boilerplate`, as expected.
The path adjustment applies only to this Python session.

#### using_name.py

The shebang was corrected to `#!/usr/bin/env python3`.

Direct execution from the repository root printed
`This module's name is: __main__` and returned exit status `0`,
inspected immediately using `echo "$?"`.

Import behaviour was checked in a fresh Python session started
from the repository root:

```bash
python3
```

At the Python prompt:

```python
import sys
sys.path.insert(0, "code")
import using_name
print(using_name.module_name())
using_name.main()
exit()
```

Importing produced no message. Printing the return value of
`module_name()` displayed `using_name`. Calling `main()` after
import printed `This module's name is: using_name`.
These results matched the expected distinction between direct
execution and import.

#### sysargv.py

The following commands were run from the repository root.
Exit statuses were inspected immediately using `echo "$?"`.

```bash
python3 code/sysargv.py
echo "$?"

python3 code/sysargv.py oak 12
echo "$?"

python3 code/sysargv.py "two words" 12
echo "$?"
```

| Arguments supplied | Reported count | Reported argument list | Exit status |
| --- | --- | --- | --- |
| None | `0` | `[]` | `0` |
| `oak 12` | `2` | `['oak', '12']` | `0` |
| `"two words" 12` | `2` | `['two words', '12']` | `0` |

All runs reported `code/sysargv.py` as the script name.
The results confirmed that arguments remain strings and quoted
text containing spaces is passed as one argument.

#### loops.py

Run from the repository root:

```bash
python3 code/loops.py
echo "$?"
```

The output was inspected in order:

| Section | Observed output |
| --- | --- |
| Range loop | Integers `0` to `4`. |
| List loop | `0`, `2`, `geronimo!`, `3.0`, `True`, `False`, each on a separate line. |
| Cumulative addition | `0`, `1`, `12`, `123`, `1234`, each on a separate line. |
| While loop | Integers `1` to `100`, then termination. |

All four sequences matched the expected values and order.
The exit status was `0`.

#### cfexercises1.py

The for-loop factorial calculation was corrected from addition to
multiplication. The recursive implementation's existing zero base case
was retained. Docstrings and explanatory comments were added, and
example calls were placed under a main guard.

Run from the repository root:

```bash
python3 code/cfexercises1.py
echo "$?"
```

The observed results matched independently predicted values:

| Check | Observed result |
| --- | --- |
| Square root of `9` | `3.0` |
| Larger of `3` and `7` | `7` |
| Equal values `5` and `5` | `5` |
| Sorting `3, 1, 2` | `[1, 2, 3]` |
| Sorting with duplicates: `2, 1, 2` | `[1, 2, 2]` |
| Three factorial methods at `0` | All returned `1`. |
| Three factorial methods at `1` | All returned `1`. |
| Three factorial methods at `5` | All returned `120`. |

Direct execution returned exit status `0`.

Import behaviour was checked in a fresh Python session started
from the repository root:

```bash
python3
```

At the Python prompt:

```python
import sys
sys.path.insert(0, "code")
import cfexercises1
print(cfexercises1.foo_4(5))
print(cfexercises1.foo_5(0))
exit()
```

Importing produced no output. The explicit calls printed `120` and `1`,
respectively. Invalid inputs and large recursive inputs were not tested.

#### cfexercises2.py

The original loop and conditional logic was retained.
Docstrings and explanatory comments were added, and demonstration
calls were moved under a main guard.

Run from the repository root:

```bash
python3 code/cfexercises2.py
echo "$?"
```

The six output groups were inspected:

| Call | Observed greeting count |
| --- | --- |
| `hello_1(12)` | `4` |
| `hello_2(12)` | `4` |
| `hello_3(3, 17)` | `14` |
| `hello_4(0)` | `5` |
| `hello_5(12)` | `8` |
| `hello_6(True, 0)` | `6`, numbered `0` to `5` |

Counts exclude the space-only separator lines.
For `hello_2(12)`, qualifying values are `3`, `7`, `8` and `11`.
The value `3` satisfies both conditions but prints only once
because the second branch uses `elif`.
Direct execution returned exit status `0`.

Import and boundary behaviour were checked in a fresh Python session
started from the repository root:

```bash
python3
```

At the Python prompt:

```python
import sys
sys.path.insert(0, "code")
import cfexercises2

print("Check 1")
cfexercises2.hello_1(0)
print("Check 2")
cfexercises2.hello_2(0)
print("Check 3")
cfexercises2.hello_3(3, 3)
print("Check 4")
cfexercises2.hello_4(15)
print("Check 5")
cfexercises2.hello_5(100)
print("Check 6")
cfexercises2.hello_6(False, 0)
print("Check 7")
cfexercises2.hello_6(True, 5)
exit()
```

Importing produced no output. Checks 1–6 produced only their separator
lines, with no greetings. Check 7 printed `hello! 5` once, followed
by its separator line. All checks terminated as expected.
Inputs known to cause non-termination were not executed.

#### control_flow.py

Run the demonstration and embedded doctests from the repository root:

```bash
python3 code/control_flow.py
echo "$?"

python3 -m doctest -v code/control_flow.py
echo "$?"
```

The demonstration printed the expected results:

```text
22 is Even!
33 is Odd!
Largest divisor among 2, 3, 4 and 5: 5
Is 59 prime? True
Primes up to 20: [2, 3, 5, 7, 11, 13, 17, 19]
```

All three doctest examples in `even_or_odd` passed.
Both commands returned exit status `0`.
The other functions are checked by the separate test script below.

#### test_control_flow.py

Run from the repository root:

```bash
python3 code/test_control_flow.py
echo "$?"
```

The script completed without output and returned exit status `0`.
Its checks covered:

| Function | Cases checked |
| --- | --- |
| `even_or_odd` | Even and odd integers, zero, a negative integer, and text rejected with `TypeError`. |
| `largest_divisor_five` | Results of `5`, `4` and `None`. |
| `is_prime` | Negative input, zero, one, the first two primes, and a composite number. |
| `find_all_primes` | An upper limit below two and the known primes through ten. |
| `count_above` | Mixed heights, values below/at/above the threshold, and an empty list. |

The threshold boundary check confirmed that values equal to the
threshold are excluded. Importing `control_flow` during the test run
produced no demonstration output.

All listed checks passed; they do not cover every possible input.

#### observations_practice.py and test_observations_practice.py

Input validation was extended to check the row-list type, individual
row types and the requested site argument. The existing two-pass
validation/deduplication and summary approach was retained.
Docstrings, comments and the known-count variable name were clarified.

After the function checks passed, the initial row-inspection block
was replaced with a sorted per-site report.

Run from the repository root:

```bash
python3 code/test_observations_practice.py
echo "$?"

python3 code/observations_practice.py
echo "$?"
```

The test script completed without output. The report printed:

```text
Site A: known_total=2, missing_count=1
Site B: known_total=0, missing_count=0
```

Both commands returned exit status `0`.

| Check group | Verified behaviour |
| --- | --- |
| Count conversion | Valid integers, known zero and missing text; invalid text, negative counts and non-text input raise `ValueError`. |
| Site summaries | Correct site selection, known totals, all-missing counts, observed zero, empty input and absent sites. |
| Duplicate handling | Repeated nonzero and missing-count records are counted once. |
| CSV inputs | Ordinary A/B and boundary C/D summaries match the expected tuples; invalid-file rows are checked separately. |
| Validation | Invalid containers, row types, fields and site arguments are rejected, including invalid records for another site. |
| Input protection | Input dictionaries and their order remain unchanged, including a duplicate-containing example. |
| Additional synthetic example | Pound Hill returns `(10, 1)` and Silwood Park returns `(0, 1)`. |

The additional records are invented test data, not real observations.


##### Prepared faulty-example critique

The test script also checks that the deliberately faulty
`suggested_total` returns 2 for A and 0 for B using the ordinary CSV.
These checks passed, but do not expose its missing-value error.

In an interactive Python session, the correct and deliberately faulty
functions were compared using the boundary CSV.

| Site | Correct known total | `suggested_total` |
| --- | --- | --- |
| C: all counts missing | `None` | `0` |
| D: observed zero | `0` | `0` |

The assertion that the correct C total is `None` passed.
The equivalent assertion for `suggested_total` raised the expected
`AssertionError`. This deliberate failure was run interactively
and was not added to the normal test script.

The faulty function starts at zero and never records whether a known
count was encountered. Ordinary A/B checks do not expose this defect;
the all-missing C boundary does. The faulty function was rejected
for reporting, and the normal test script was rerun successfully.

The report and test script were subsequently rerun successfully in the fresh clone. Comparison with a peer's fresh run remains pending.

#### debugme.py

A temporary version without exception handling was used to inspect
the state immediately before division by zero. A conditional
`breakpoint()` was placed after decrementing y, when y reached zero.

The temporary script was run from the repository root:

```bash
python3 code/debugme.py
```

At the Pdb prompt, `p i`, `p x`, `p y`, `p z` and `l` were used.

| Variable | Observed value |
| --- | --- |
| `i` | `19` |
| `x` | `20` |
| `y` | `0` |
| `z` | `20.0` |

The next division would use a zero denominator. The value of z was
left over from the preceding successful division, not a result
of dividing by zero. The debugger was exited using `q`, with
confirmation to terminate the process.

The temporary breakpoint was removed and the exception-handling
version restored. A specific `except ZeroDivisionError` was retained;
the broad exception handler was removed so unexpected errors remain
visible. Docstrings and a guarded demonstration were added.

The final version was checked with:

```bash
python3 code/debugme.py
echo "$?"
```

It printed 19 successful-division messages, one division-by-zero
message and `Returned value: 20.0`. It completed without pausing
and returned exit status `0`.

### Additional classroom exercises: R

#### basic_io.R

Corrected the append path from `results/MyData,csv` to
`results/MyData.csv`, added output-directory creation and clarified comments.
The original sequence of file-writing demonstrations was retained.

The Rscript command under Usage printed `Script complete!`, produced
the expected append-header warning and returned exit status `0`.
Sourcing the script in an
`R --vanilla` session also completed successfully.

Interactive checks confirmed that:

- The initial CSV contained column names and row names.
- Appending added a header and the first data record, increasing the
  line count by two.
- The next CSV write overwrote the appended content.
- The final table write omitted column names and used spaces as separators.

The final output was read back using `read.table()` with `header = FALSE`
and `row.names = 1`. After restoring the column names, its dimensions and
data matched the input using `all.equal()`.

Running the script again produced the same final output file,
without accumulating extra rows.

#### boilerplate.R

Clarified comments and spacing while retaining the original function
and its numeric and character examples.

The Rscript command documented under Usage completed with exit
status `0`, printing the argument descriptions and the expected
numeric and character vectors.

Sourcing the script in a clean R session also succeeded.
`ls()` confirmed that `MyFunction` existed, and `class(MyFunction)`
returned `"function"`. Explicit calls returned `c(1, 2)` and
`c("riki", "Tiki")`, alongside the printed argument descriptions.

#### control_flow.R

Corrected the square-message spelling, standardised formatting and
clarified comments. Updated the conditional message to match `<= 0.5`,
retaining the original conditions and loops.

Both execution methods under Usage succeeded. Rscript returned exit
status `0`, and sourcing was checked in a clean R session.

The outputs matched expectations: the TRUE-branch message, square
descriptions for integers 1–10, three species names, `"a"`, `"bc"`,
`"def"`, and the while-loop squares from 1 to 100. Neither recorded run
printed the random conditional message, which is valid behaviour.

Separate interactive checks used `a <- FALSE` and repeated the
conditional block, confirming the FALSE-branch message. Testing
`z <= 0.5` with 0.4, 0.5 and 0.6 produced the conditional message for
the first two values only, confirming that equality is included.

#### r_conditionals.R

Added a separate prime case for 2, avoiding the incorrect divisor
sequence `2:1`. Added handling for negative prime inputs and
non-positive power-of-2 inputs. Retained the original messages for
0 and 1 in the prime function. Explicit printing makes demonstration
results visible with both execution methods.

The Rscript command under Usage returned exit status `0`.
Sourcing in a clean R session also printed the three expected
demonstration results.

Additional interactive calls produced the expected results:

| Function | Inputs checked | Results |
| --- | --- | --- |
| `is.even` | 5, 0, -2 | Odd, even, even |
| `is.power2` | 1, 2, 8 | Powers of 2 |
| `is.power2` | 3, 0, -2 | Not powers of 2 |
| `is.prime` | -1 | Not prime |
| `is.prime` | 0, 1 | Original zero and unit messages |
| `is.prime` | 2, 3 | Prime |
| `is.prime` | 4, 9 | Composite |

#### break.R

Corrected misleading comments and standardised indentation while
retaining the original loop and `break` condition.

Both execution methods under Usage printed values from 0 to 9 and
terminated normally. Rscript returned exit status `0`.

After sourcing in a clean R session, entering `i` returned `10`,
confirming that the loop exited before printing the stopping value.

#### next.R

Corrected the comment to identify even numbers and clarified
indentation with braces, retaining the original `next` behaviour.

Both execution methods under Usage printed only 1, 3, 5, 7 and 9.
Rscript returned exit status `0`.

After sourcing in a clean R session, entering `i` returned `10`,
confirming that the loop reached its final iteration while skipping
the print statement for even numbers.

#### try.R

Retained the textbook structure and added the preallocated-list
loop and explicit result inspection. The uncaught-error example
remains commented out. The histogram is saved under `results/`.

Both execution methods under Usage completed. Rscript returned
exit status `0`, and the histogram PDF existed with nonzero size.

In the recorded runs, both methods retained 15 results:

| Method | Successful attempts | Failed attempt positions |
| --- | --- | --- |
| `lapply()` | 13 | 5, 12 |
| `for` loop | 12 | 7, 11, 13 |

After sourcing in a clean R session, these additional checks were run:

```r
class(result)
length(result)
class(result[[7]])
class(result[[15]])
```

They returned `"list"`, `15`, `"try-error"` and `"character"`,
respectively, confirming that a failed attempt was stored and
later attempts still completed.

The histogram PDF was opened and visually inspected.
The title, axes and bars were readable, with no obvious clipping.
The displayed bin frequencies totalled 50, matching the size of
popn. This figure shows the original generated population,
not the means from the subsequent sampling attempts.

#### browse.R

Removed the unrelated commented-out example, clarified comments
and formatting, and directed the plot to `results/`.
The growth calculation and breakpoint after each update were retained.

Interactive inspection in a clean R session showed:

- At the first pause, `t` was 2; `N0`, `r` and `generations` were
  1, 1 and 10.
- The first two population values were 1 and approximately 2.718282,
  with later entries still `NA`.
- After stepping to `t = 5`, the first five values were approximately
  1, 2.718282, 7.389056, 20.085537 and 54.598150.

Continuing with `c` through the remaining pauses returned to the
ordinary R prompt. The saved version generated the PDF successfully.

Additional checks were:

```r
file.exists("results/browse_exponential.pdf")
file.info("results/browse_exponential.pdf")$size
dev.cur()
```

They returned `TRUE`, 4615 bytes and `null device 1`, respectively.

Visual inspection of the generated plot confirmed a readable title
and axes, with an increasing trajectory consistent with exponential
growth. The final plotted value was approximately 8100.

#### observations_practice.R

The script was run and sourced in an R 4.5.2 session started with
`R --vanilla` from the repository root. On 27 November 2026, its
summaries were independently checked against the supplied CSV records.

| Site | Counts after exact-row deduplication | Known total | Missing count |
| --- | --- | --- | --- |
| A | 2 and NA | 2 | 1 |
| B | 0 | 0 | 0 |
| C | NA and NA, on different dates | NA | 2 |
| D | 0 | 0 | 0 |

These results matched the embedded assertions. A's duplicate record
contributes only once. D's duplicate zero record is also removed.
Both C records remain because their dates differ.

The supplied invalid CSV triggered the expected error for -1.
Because reading stops at the first invalid count, many was checked
separately using a temporary CSV containing the second input record.

To reproduce the additional checks, start `R --vanilla` from the
repository root and enter:

```r
source("code/observations_practice.R")

invalid_data <- read.csv(
    "data/bootcamp_observations_invalid.csv",
    colClasses = "character"
)

temporary_csv <- tempfile(fileext = ".csv")
write.csv(
    invalid_data[2, , drop = FALSE],
    temporary_csv,
    row.names = FALSE
)

many_result <- try(read_observations(temporary_csv), silent = TRUE)

stopifnot(
    inherits(many_result, "try-error"),
    grepl("found many", as.character(many_result), fixed = TRUE)
)

print(many_result)
unlink(temporary_csv)

previous_summary <- all_summaries
source("code/observations_practice.R")
stopifnot(identical(previous_summary, all_summaries))
print("Repeated-run summaries match.")

q(save = "no")
```

The many check passed and printed the expected caught error.
The repeated-run comparison also passed, printing
`Repeated-run summaries match.` No supplied CSV was edited by
these checks.

The regenerated PDF was opened and inspected. It showed A at 2,
B and D at 0, and no point for C. The subtitle correctly explained
C's all-missing counts. The title, axes and site labels were readable,
with no obvious clipping or overlap.

R reported incomplete-final-line warnings because the supplied CSV
files lack a trailing newline. The records were read correctly, and
the supplied files were retained unchanged.

##### Critique and comparison with Python

Missing observations and observed zeros have different meanings.
Removing missing values is useful when summing known counts, but
`sum(c(NA_integer_, NA_integer_), na.rm = TRUE)` returns zero even
though no count was observed. The summary must first distinguish
an all-missing site from one containing a known zero. The assertion
that C's total is NA detects this error; D checks the observed-zero case.

Exact duplicate rows must be removed before summarising. Otherwise,
A's repeated count of 2 produces a total of 4 instead of 2.
Checking only the number of sites would miss this error because
the duplicate does not introduce another site. The assertion that
A's total equals 2 detects it. Removing duplicate count values alone
is inappropriate: different observations can legitimately have
the same count.

Both R and Python should apply the same validation, exact-row
deduplication and missing-versus-zero rules. Their representations
differ: R uses NA for missing counts and all-missing totals, whereas
the Python implementation uses None. R's sum() defaults to propagating
NA; using na.rm = TRUE therefore requires an explicit all-missing check.

An informative validation error identifies the file, CSV line,
column, offending value and expected format. For the original many
entry, an appropriate message would be:

    bootcamp_observations_invalid.csv: CSV line 3, column 'count':
    found 'many'; expected an empty field or a non-negative integer.

The separate many test used a temporary file containing only that
record, so its reported CSV line was 2, including the header.
Invalid values are reported rather than silently replaced.

#### data_wrang.R

The Usage command returned exit status `0` on 27 November 2026.
Additional checks were performed in R 4.5.2, starting with
`R --vanilla` from the repository root.

| Check | Observed result |
| --- | --- |
| Input structure | Raw matrix: 45 rows × 60 columns; transposed matrix: 60 × 45. |
| Long-table structure | 2419 rows × 6 columns, representing 41 species across 59 sampled quadrats. |
| Counts | Integer, non-negative and without missing values. |
| Record uniqueness | No duplicated combination of the four identifiers and species. |
| Raw-to-long comparison | Every species count and its four sample identifiers matched the raw table, with blanks treated as zero. |
| CSV readback | Saved contents matched the in-memory table after converting factors to character for comparison. |
| Repeated execution | Both the in-memory table and CSV text were identical between runs. |

To reproduce the additional checks, start a clean R session from
the repository root and enter:

```r
source("code/data_wrang.R")

stopifnot(
    identical(dim(MyWrangledData), c(2419L, 6L)),
    !anyNA(MyWrangledData),
    all(MyWrangledData$Count >= 0),
    anyDuplicated(MyWrangledData[1:5]) == 0L
)

raw <- read.csv(
    "data/pound_hill_data.csv",
    header = FALSE,
    colClasses = "character",
    na.strings = ""
)

for (i in 5:nrow(raw)) {
    actual <- MyWrangledData[
        as.character(MyWrangledData$Species) == raw[i, 1],
    ]

    expected <- as.integer(unlist(raw[i, -1], use.names = FALSE))
    expected[is.na(expected)] <- 0L
    stopifnot(identical(actual$Count, expected))

    for (j in 1:4) {
        stopifnot(identical(
            as.character(actual[[j]]),
            unlist(raw[j, -1], use.names = FALSE)
        ))
    }
}

saved <- read.csv(
    "results/pound_hill_long.csv",
    colClasses = c(rep("character", 5), "integer")
)
expected_table <- MyWrangledData
expected_table[1:5] <- lapply(expected_table[1:5], as.character)
stopifnot(identical(saved, expected_table))

previous <- MyWrangledData
previous_csv <- readLines("results/pound_hill_long.csv")
source("code/data_wrang.R")
stopifnot(
    identical(previous, MyWrangledData),
    identical(previous_csv, readLines("results/pound_hill_long.csv"))
)

q(save = "no")
```

All corresponding checks passed without assertion errors. Normal execution was subsequently verified in the fresh clone.

#### data_wrang_tidy.R

Checks were completed on 27 November 2026 in R 4.5.2, using an
`R --vanilla` session started from the repository root.

| Check | Observed result |
| --- | --- |
| Small-table transformation | Two sites and two species produced the four expected records, preserving counts and zeros. |
| Structure and types | 2419 rows × 6 columns; five factors and integer Count. |
| Counts and record uniqueness | No missing values, negative counts or duplicate sample–species combinations. |
| Comparison with reshape2 | All records matched after normalising table types, categorical columns and row order. |
| CSV readback | Saved contents matched the tidy table after converting factors to character. |
| Repeated execution | The in-memory result and CSV text were identical between runs. |

To reproduce these checks, start a clean R session from the repository
root and enter the following. The comparison also requires `reshape2`.

```r
small <- data.frame(
    Site = c("A", "B"),
    Species1 = c(2L, 0L),
    Species2 = c(0L, 3L)
)

small_long <- tidyr::pivot_longer(
    small,
    cols = -Site,
    names_to = "Species",
    values_to = "Count"
)

stopifnot(
    identical(small_long$Site, c("A", "A", "B", "B")),
    identical(
        small_long$Species,
        c("Species1", "Species2", "Species1", "Species2")
    ),
    identical(small_long$Count, c(2L, 0L, 0L, 3L))
)

source("code/data_wrang.R")
reshape_result <- MyWrangledData

source("code/data_wrang_tidy.R")
tidy_result <- MyWrangledData

stopifnot(
    identical(dim(tidy_result), c(2419L, 6L)),
    identical(
        names(tidy_result),
        c("Cultivation", "Block", "Plot", "Quadrat", "Species", "Count")
    ),
    all(vapply(tidy_result[1:5], is.factor, logical(1))),
    is.integer(tidy_result$Count),
    !anyNA(tidy_result),
    all(tidy_result$Count >= 0),
    anyDuplicated(tidy_result[1:5]) == 0L
)

normalise <- function(x) {
    x <- as.data.frame(x)
    x[1:5] <- lapply(x[1:5], as.character)
    x <- x[do.call(order, x[1:5]), ]
    rownames(x) <- NULL
    return(x)
}

stopifnot(identical(
    normalise(reshape_result),
    normalise(tidy_result)
))

saved <- read.csv(
    "results/pound_hill_long.csv",
    colClasses = c(rep("character", 5), "integer")
)

expected <- as.data.frame(tidy_result)
expected[1:5] <- lapply(expected[1:5], as.character)
stopifnot(identical(saved, expected))

previous_csv <- readLines("results/pound_hill_long.csv")
source("code/data_wrang_tidy.R")

stopifnot(
    identical(tidy_result, MyWrangledData),
    identical(previous_csv, readLines("results/pound_hill_long.csv"))
)

q(save = "no")
```

All checks passed without warnings or assertion errors.
The reshape2 reference result had previously been checked against
every raw species count and its sample identifiers.

Normal execution was subsequently verified in the fresh clone.
Creation of an absent `results/` directory was reviewed in the code
but not separately tested.


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

### Additional classroom exercises: Shell

- `ConcatenateTwoFiles.sh` compares path strings when checking for
  overlapping inputs and output. Different paths referring to the same
  file, including symbolic and hard links, are not detected.
  The caller must ensure the output is a separate file.
- `ConcatenateTwoFiles.sh` overwrites existing output. A processing
  failure may leave a partial output; the previous output is not restored.
- `tiff2_png.sh` handles only lowercase `.tif` matches in the current
  directory. It does not explicitly handle no matching files,
  option-like filenames, output collisions or conversion failures.
  Existing PNG outputs may be overwritten, and the script's final
  exit status does not establish that every conversion succeeded.

### Additional classroom exercises: Python

- Observation dates are checked only for non-empty text; calendar
  validation and whitespace normalisation are outside this exercise.
- Exact-duplicate removal is a teaching assumption, not a universal
  rule for ecological observations.
- Known-count totals exclude missing observations and do not estimate
  their contribution.
- `suggested_total` is deliberately incorrect for all-missing data
  and must not be used as the reporting implementation.
- `debugme.py` is a teaching demonstration using `x = 20`, not a
  general numerical algorithm. Its function assumes an integer
  input of at least two and does not validate other inputs.
  Catching division by zero preserves the previous successful
  result; it does not make the failed division valid.

### Additional classroom exercises: R
- `r_conditionals.R` assumes single finite integer inputs and does not
  validate other types. Its logarithm-based power check and divisor
  sequence are intended for small teaching examples, rather than
  large-number computation.
- `observations_practice.R` checks dates only for non-empty text;
  it does not validate calendar dates or normalise whitespace.
- Exact-row deduplication is an assumption of this exercise, rather
  than a general rule for ecological observations.
- Known-count totals exclude missing observations and do not estimate
  their contribution.
- The figure uses a fixed vertical range of 0–3, suitable for the
  supplied data; larger totals would require adjusting this range.


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

### Assignment 4: cumulative revision

During 2–27 November 2026, I used ChatGPT to clarify coursework
requirements and formative feedback, explain programming concepts
and error messages, review existing code, suggest targeted checks,
and help organise and edit the README.

ChatGPT also provided example verification commands, including
commands for comparing outputs and checking a fresh clone.
I ran the checks locally, inspected terminal output, tables and
figures, and compared selected results with calculations performed
separately from the functions being checked. I reviewed suggestions against
the course materials before adopting them.