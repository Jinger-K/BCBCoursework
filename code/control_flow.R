# Demonstrate conditional statements, for loops and a while loop.
# Run from the coursework project root:
# Rscript code/control_flow.R

# Select a branch using a logical value.
a <- TRUE
if (a) {
    print("a is TRUE")
} else {
    print("a is FALSE")
}

# Print a message only when the random value is at most 0.5.
z <- runif(1)
if (z <= 0.5) {
    print("Less than or equal to a half")
}

# Calculate and print the squares of integers from 1 to 10.
for (i in 1:10) {
    j <- i * i
    print(paste(i, "squared is", j))
}

# Loop over a vector of species names.
for (species in c("Heliodoxa rubinoides",
                  "Boissonneaua jardini",
                  "Sula nebouxii")) {
    print(paste("The species is", species))
}

# Loop over an existing character vector.
v1 <- c("a", "bc", "def")
for (i in v1) {
    print(i)
}

# Increment before printing, producing squares from 1 to 100.
i <- 0
while (i < 10) {
    i <- i + 1
    print(i^2)
}