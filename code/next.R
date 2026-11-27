# Demonstrate skipping even numbers using next.
# Run from the coursework project root:
# Rscript code/next.R

for (i in 1:10) {
    # Skip the remaining statements for even numbers.
    if (i %% 2 == 0) {
        next
    }
    print(i)
}