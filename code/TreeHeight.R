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

# Calculate the heights
trees$Tree.Height.m <- TreeHeight(trees$Angle.degrees, trees$Distance.m)

# Write into csv
write.csv(trees, "results/TreeHts.csv", row.names = FALSE)
