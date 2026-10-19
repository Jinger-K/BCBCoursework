# This function calculates heights of trees given distance of each tree
# from its base and angle to its top, using the trigonometric formula
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees: The angle of elevations of tree
# distance: The distance from base of tree (e.g., meters)
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
trees <- read.csv("data/trees.csv")


# Inspect the header and a few rows
print(names(trees))
print(head(trees)) 

# Check for the three required columns
required_columns <- c("Species", "Distance.m", "Angle.degrees")

if(!all(required_columns %in% names(trees))) {
    stop("Input file does not have all three require columns: Species, Distance.m and Angle.degrees.")
}

# Check for mumeric finite Distance.m and Angle.degrees
if(!is.numeric(trees$Distance.m)) {
    stop("Distance.m must be numeric.")
}
if(!is.numeric(trees$Angle.degrees)) {
    stop("Angle.degrees must be numeric.")
}

# Check if the values are finite in case it fails if()
if(!all(is.finite(trees$Distance.m))) {
    stop("Distance.m must and only contain finite values.")
}
if(!all(is.finite(trees$Angle.degrees))) {
    stop("Angle.degrees must and only contain finite values.")
}

# Check if 0 < Distance.m <= 100
if(!all(trees$Distance.m > 0 & trees$Distance.m <= 100)) {
    stop("Distance.m must be greater than 0 and no greater than 100.")
}

# Check if 0 < Angle.degrees < 90
if(!all(trees$Angle.degrees > 0 & trees$Angle.degrees < 90)) {
    stop("Angle.degrees must be greater than 0 and less than 90.")
}



# Calculate the heights
trees$height_m <- TreeHeight(trees$Angle.degrees, trees$Distance.m)

# Create the result directory if needed
if(!dir.exists("results")) {
    dir.create("results")
}
# Write into csv
write.csv(trees, "results/TreeHts.csv", row.names = FALSE) # The file will be replaced on rerun
