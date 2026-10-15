# Reading and inspecting ecological observation data

# observations <- read.csv(
#    "data/bootcamp_observations.csv",
#    colClasses = "character", na.strings = "", check.names = FALSE
#)

# Inspect the data
# str(observations)

# print(observations)

# read_observations(path)z
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

# Deduplicate and summarise
summarise_observations <- function(data) {

    # Duplicate observations

    observations <- paste(data$site, data$date, data$count)

    unique <- c()
    keep <- c()

    for (i in 1:length(observations)) {
        if(!(observations[i] %in% unique)){
            unique <- c(unique, observations[i])
            keep <- c(keep, i)
        }
    }
    
    unique_data <- data[keep, ]

    # Summarise sites
    sites <- c()

    for (site in unique_data$site) {
        if (!(site %in% sites)) {
            sites <- c(sites, site)
        }
    }


    for (site in sites) {
        counts <- unique_data$count[unique_data$site == site]

        #  Summarise total known and missing count
        total_known = 0
        missing_count = 0
        flag = TRUE

        for (count in counts) {

            if (is.na(count)) {
                missing_count = missing_count + 1
            } else {
                total_known = total_known + count
                flag = FALSE
            }

        }

        if (flag) {
            total_known = NA
        }

        print(paste(site, "(", total_known, ",", missing_count, ")"))

    }

}

summarise_observations(valid_data)