#!/bin/bash

# Require two input paths and one output path.
if [[ $# -ne 3 ]]; then
    printf 'Usage: %s input_file_1 input_file_2 output_file\n' "$0" >&2
    exit 2
fi

# Both inputs must be readable regular files.
if [[ ! -f "$1" || ! -r "$1" ]]; then
    printf 'Error: first input must be a readable regular file: %s\n' "$1" >&2
    exit 1
fi

if [[ ! -f "$2" || ! -r "$2" ]]; then
    printf 'Error: second input must be a readable regular file: %s\n' "$2" >&2
    exit 1
fi

# Reject identical path strings before redirection can erase an input.
if [[ "$3" == "$1" || "$3" == "$2" ]]; then
    printf 'Error: output path must differ from both input paths\n' >&2
    exit 1
fi

# Write the first input, replacing any previous output.
cat "$1" > "$3"

if [[ $? -ne 0 ]]; then
    printf 'Error: could not write the first input to %s\n' "$3" >&2
    exit 1
fi

# Append the second input only after the first step succeeds.
cat "$2" >> "$3"

if [[ $? -ne 0 ]]; then
    printf 'Error: could not append the second input to %s\n' "$3" >&2
    exit 1
fi

echo "Merged File is"
cat "$3"