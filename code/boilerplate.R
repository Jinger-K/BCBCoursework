# Demonstrate a function with two arguments and a returned vector.
# Run from the coursework project root:
# Rscript code/boilerplate.R

# Print each argument's value and class, then return their combined vector.
MyFunction <- function(Arg1, Arg2) {
    print(paste("Argument", as.character(Arg1), "is a", class(Arg1)))
    print(paste("Argument", as.character(Arg2), "is a", class(Arg2)))

    return(c(Arg1, Arg2))
}

# Demonstrate numeric and character arguments.
MyFunction(1, 2)
MyFunction("riki", "Tiki")