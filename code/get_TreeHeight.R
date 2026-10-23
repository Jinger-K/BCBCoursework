# Calculate tree heights using:
#
# height = distance * tan(degrees * pi / 180)
#
# ARGUMENTS
# degrees: The angle of elevations of tree, measured from horizontal in degrees
# distance: Horizontal distance from the observer to the tree, in metres
#
# OUTPUT
# The heights of the tree, same units as "distance"

# Define the function to calculate tree heights
TreeHeight <- function(degrees, distance){
    radians <- degrees * pi /180
    height <- distance * tan(radians)
    print(paste("Tree height is;", height))

    return (height)
}

# Load the data

input_path <- commandArgs(trailingOnly = TRUE)

# Check the number of argument(s)
if(length(input_path) != 1) {
    stop("There must be one input path.")
}

# Check that the input file exists and is readable
if(!file.exists(input_path[1])) {
    stop("File doesn't exist.")
}        

if (dir.exists(input_path[1])) {
    stop("Input path is a directory; please provide a CSV file.")
}

if(file.access(input_path[1], mode = 4) != 0) {
    stop("Input file cannot be read.")
}


trees <- read.csv(input_path[1])


# Inspect the header and a few rows
print(names(trees))
print(head(trees)) 

# Check for the three required columns
required_columns <- c("Species", "Distance.m", "Angle.degrees")

if(!(all(required_columns %in% names(trees)) && ncol(trees) == 3)) {
    stop("Input file must contain three required columns: Species, Distance.m and Angle.degrees.")
}

# Check for numeric finite Distance.m and Angle.degrees
if(!is.numeric(trees$Distance.m)) {
    stop("Distance.m must be numeric.")
}
if(!is.numeric(trees$Angle.degrees)) {
    stop("Angle.degrees must be numeric.")
}

# Check if the values are finite in case it fails if()
if(!all(is.finite(trees$Distance.m))) {
    stop("Distance.m must contain only finite values.")
}
if(!all(is.finite(trees$Angle.degrees))) {
    stop("Angle.degrees must contain only finite values.")
}

# Check if 0 < Distance.m <= 100
if(!all(trees$Distance.m > 0 & trees$Distance.m <= 100)) {
    stop("Distance.m must be greater than 0 and no greater than 100.")
}

# Check if 0 < Angle.degrees < 90
if(!all(trees$Angle.degrees > 0 & trees$Angle.degrees < 90)) {
    stop("Angle.degrees must be greater than 0 and less than 90.")
}

# Make sure the columns are organised in the required order
trees <- trees[, required_columns]

browser()

# Calculate the heights
trees$height_m <- TreeHeight(trees$Angle.degrees, trees$Distance.m)

# Create the result directory if needed
if(!dir.exists("results")) {
    dir.create("results")
}

# Build the output path from the input filename
filename <- basename(input_path[1])
filename <- sub("\\.csv$", "", filename)
output_path <- file.path("results",paste0(filename, "_treeheights.csv"))

# Prevent overwriting the input file
if(normalizePath(input_path[1], mustWork = TRUE) == normalizePath(output_path, mustWork = FALSE)) {
    stop("Input path and output path are the same.")
}


# Write into csv
write.csv(trees, output_path, row.names = FALSE) # The file will be replaced on rerun
