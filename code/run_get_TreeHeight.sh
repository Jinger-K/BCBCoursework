#!/bin/bash

# Run the code
Rscript code/get_TreeHeight.R data/trees.csv

# Check exit status
if [ "$?" -ne 0 ]; then
    exit 1
fi