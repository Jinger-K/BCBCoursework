#!/bin/bash
# Author: Ke Jiang kj726@ic.ac.uk
# Script: csvtospace.sh
# Desc: replace commas with spaces
# Arguments : 1-> csv file
# Date: Oct 2026

# Accept exactly one readable csv input file and support paths containing spaces
if [[ $# -ne 1 ]]; then
    printf 'Please provide exactly one input file path after the script name.\n' >&2
    exit 2
fi

# Check file type and readability
if [[ -f "$1" && -r "$1" ]]; then
    output_file="../results/$(basename "$1").txt"
else
    printf 'Error: not a readable file: %s\n' "$1" >&2
    exit 1
fi

# Create results directory if needed
mkdir -p ../results

if [[ $? -ne 0 ]]; then
    printf 'Error: cannot create the results directory\n' >&2
    exit 1
fi


printf 'Creating a space delimited version of %s ... \n' "$1"

# Preserve empty fields and replace old output. 
tr ',' ' ' < "$1" > "$output_file"

# Stop on failure
if [[ $? -ne 0 ]]; then
    printf 'Error: conversion failed: %s\n' "$1" >&2
    exit 1
fi

echo "Done!"

exit 0