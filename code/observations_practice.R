# Reading and inspecting ecological observation data

# observations <- read.csv(
#    "data/bootcamp_observations.csv",
#    colClasses = "character", na.strings = "", check.names = FALSE
#)

# Inspect the data
# str(observations)

# print(observations)

# read_observations(path)
# what should ir receive: observation csv file path
# what should it check: cthe exact column names, reject empty sites or dates
# what should it return: a clean data frame

read_observations <- function(path) {

    # Check if the file exists
    if(!file.exists(path)) {
        stop("File does not exist")
    }
    
    # Read the data
    observations <- read.csv(
    path, colClasses = "character", na.strings = "", check.names = FALSE
    )

    # Check the column names
    column_names <- names(observations)
    
    if (!(length(column_names) == 3 && column_names[1] == "site" && column_names[2] == "date" && column_names[3] == "count")) {
        stop("Column names are incorrect")
    }

    # Check for missing site values
    if(any(is.na(observations$site))){
        stop("Missing site values")
    }

    # Check for missing date values
    if(any(is.na(observations$date))){
        stop("Missing date values")
    }

    # Check and convert for count values
    counts <- observations$count

    for (value in counts) {
        if (!is.na(value)) {
            if(!grepl("^(0|[1-9][0-9]*)$", value)){
                stop(paste("Invalid count:", value))
            }
        }
    }

    # Convert count as integers
    observations$count <- as.integer(observations$count)

    # Return the data frame
    return (observations)

}


# Test the valid data

valid_data <- read_observations("data/bootcamp_observations.csv")

str(valid_data)
print(valid_data)