#!/bin/bash

# Convert lowercase .tif files in the current working directory.
for filename in *.tif
do
    echo "Converting $filename"
    # Preserve the filename stem and replace the .tif suffix with .png.
    convert "$filename" "$(basename "$filename" .tif).png"
done