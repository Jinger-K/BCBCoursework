observations <- read.csv(
    "data/bootcamp_observations.csv",
    colClasses = "character", na.strings = "", check.names = FALSE
)
str(observations)
print(observations)