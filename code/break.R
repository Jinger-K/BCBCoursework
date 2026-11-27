# Demonstrate exiting a while loop using break.
# Run from the coursework project root:
# Rscript code/break.R

i <- 0
while (i < Inf) {
    if (i == 10) {
        # Exit before printing 10.
        break
    } else {
        cat("i equals ", i, "\n")
        i <- i + 1
    }
}