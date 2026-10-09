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
