# Demonstrate catching errors during repeated sampling.
# Run from the coursework project root:
# Rscript code/try.R

doit <- function(x) {
    temp_x <- sample(x, replace = TRUE)

    # Require more than 30 distinct sampled values.
    if (length(unique(temp_x)) > 30) {
        print(paste("Mean of this sample was:", as.character(mean(temp_x))))
    } else {
        stop("Couldn't calculate mean: too few unique values!")
    }
}

set.seed(1345)
popn <- rnorm(50)

# Save the original histogram example under results/.
if (!dir.exists("results")) {
    dir.create("results")
}

pdf("results/try_population.pdf")
hist(popn)
dev.off()

# Try separately at the R prompt to observe an uncaught error:
# lapply(1:15, function(i) doit(popn))

# Catch errors and continue through all 15 attempts.
result <- lapply(1:15, function(i) try(doit(popn), FALSE))

print(class(result))
print(result)

# Repeat using the textbook's preallocated list and for loop.
result <- vector("list", 15)
for (i in 1:15) {
    result[[i]] <- try(doit(popn), FALSE)
}

print(class(result))
print(result)