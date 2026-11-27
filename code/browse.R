# Demonstrate interactive debugging with browser().
# From an R session at the coursework project root:
# source("code/browse.R")

# Return a population vector for the requested number of generations.
# This teaching example assumes generations is an integer of at least 2.
Exponential <- function(N0 = 1, r = 1, generations = 10) {
    N <- rep(NA, generations)
    N[1] <- N0

    for (t in 2:generations) {
        N[t] <- N[t - 1] * exp(r)

        # Inspect the population immediately after each update.
        browser()
    }

    return(N)
}

# Open the PDF device, then run the interactive simulation and plot.

if (!dir.exists("results")) {
    dir.create("results")
}

pdf("results/browse_exponential.pdf")
plot(Exponential(), type = "l", main = "Exponential growth")
dev.off()