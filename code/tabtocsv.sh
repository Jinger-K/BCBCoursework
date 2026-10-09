#!/bin/bash
# Author: Ke Jiang kj726@ic.ac.uk
# Script: tabtocsv.sh
# Desc: substitute the tabs in the files with commas
#       saves the output into a .csv file
# Arguments : 1-> tab delimited file
# Date: Oct 2026

# Accept exactly one readable tab-delimited input file and support paths containing spaces
if [[ $# -ne 1 ]]; then
    printf 'Please provide exactly one input file path after the script name.\n' >&2
    exit 2
fi

# Check file type and readability
if [[ -f "$1" && -r "$1" ]]; then
    output_file="../results/$(basename "$1").csv"
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


echo 'Creating a comma delimited version of %s ... \n' "$1"

# cat $1 | tr -s "\t" "," >> $1.csv # Appends output to the file, cauding duplicate row on returns / unquoted paths can split at spaces / unquoted variable can turn wildcard characters into matching file paths
# Preserve empty fields and replace old output. 
tr '\t' ',' < "$1" > "$output_file"

# Stop on failure
if [[ $? -ne 0 ]]; then
    printf 'Error: conversion failed: %s\n' "$1" >&2
    exit 1
fi

echo "Done!"

exit 0