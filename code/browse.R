## Define nested functions
#outer_function <- function(a) {
#    middle_function(a)
#}

#middle_function <- function(b) {
#    inner_function(b)
#}

#inner_function <- function(c) {
#    # Intentional error: division by zero
#    result <- c / d
#    return(result)
#}

## Call the outer function
#outer_function(1)

Exponential <- function(N0 = 1, r = 1, generations = 10) {
    # run a simulation of exponantial growth
    # returns a vector of length generations

    N <- rep(NA, generations) # Creates a vector of NA

    N[1] <- N0
    for (t in 2:generations) {
        N[t] <- N[t-1] * exp(r)
        browser()
    }
    return (N)
}

plot(Exponential(), type="l", main="Exponential growth")