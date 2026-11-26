#!/bin/bash

# Require exactly one input file path.
if [[ $# -ne 1 ]]; then
    printf 'Usage: %s input_file\n' "$0" >&2
    exit 2
fi

# Reject directories, missing files and unreadable files.
if [[ ! -f "$1" || ! -r "$1" ]]; then
    printf 'Error: input must be a readable regular file: %s\n' "$1" >&2
    exit 1
fi

# Count newline characters; an unterminated final line is not counted.
NumLines=$(wc -l < "$1")

# Check immediately so later output commands cannot hide a counting failure.
if [[ $? -ne 0 ]]; then
    printf 'Error: could not count newlines in %s\n' "$1" >&2
    exit 1
fi

echo "The file $1 has $NumLines lines"
echo