# Demonstrate conditional statements inside functions.
# Run from the coursework project root:
# Rscript code/r_conditionals.R
# Inputs are single finite integers.

# Return a message describing whether the integer is even or odd.
is.even <- function(n) {
    if (n %% 2 == 0) {
        return(paste(n, "is even!"))
    } else {
        return(paste(n, "is odd!"))
    }
}

# Check powers of 2 with non-negative integer exponents, including 1.
is.power2 <- function(n) {
    # Avoid taking the logarithm of zero or a negative number.
    if (n <= 0) {
        return(paste(n, "is not a power of 2!"))
    }

    if (log2(n) %% 1 == 0) {
        return(paste(n, "is a power of 2!"))
    } else {
        return(paste(n, "is not a power of 2!"))
    }
}

# Check primality while retaining the original messages for 0 and 1.
is.prime <- function(n) {
    if (n < 0) {
        return(paste(n, "is not a prime!"))
    } else if (n == 0) {
        return(paste(n, "is a zero!"))
    } else if (n == 1) {
        return(paste(n, "is just a unit!"))
    } else if (n == 2) {
        return(paste(n, "is a prime!"))
    }

    # For n >= 3, check possible divisors from 2 through n - 1.
    ints <- 2:(n - 1)

    if (all(n %% ints != 0)) {
        return(paste(n, "is a prime!"))
    } else {
        return(paste(n, "is a composite!"))
    }
}

# Original demonstration calls.
print(is.even(6))
print(is.power2(4))
print(is.prime(3))