# Read, validate and summarise ecological observations.
# Run from the coursework project root:
# Rscript code/observations_practice.R

read_observations <- function(path) {
    if (!file.exists(path)) {
        stop(paste("File does not exist:", path))
    }

    # Read text first so counts are validated before conversion.
    observations <- read.csv(
        path,
        colClasses = "character",
        na.strings = "",
        check.names = FALSE
    )

    column_names <- names(observations)

    if (!(length(column_names) == 3 &&
          column_names[1] == "site" &&
          column_names[2] == "date" &&
          column_names[3] == "count")) {
        stop(paste(path, ": expected columns site,date,count"))
    }

    if (any(is.na(observations$site) | observations$site == "")) {
        stop(paste(path, ": missing site values"))
    }

    if (any(is.na(observations$date) | observations$date == "")) {
        stop(paste(path, ": missing date values"))
    }

    # Track CSV line numbers, including the header.
    csv_line <- 1
    for (value in observations$count) {
        csv_line <- csv_line + 1

        if (!is.na(value)) {
            if (!grepl("^(0|[1-9][0-9]*)$", value)) {
                stop(paste(
                    path, ": CSV line", csv_line,
                    ", column count: found", value,
                    "; expected an empty field or a non-negative integer"
                ))
            }
        }
    }

    counts <- as.integer(observations$count)

    # Do not mistake a failed integer conversion for missing data.
    if (any(!is.na(observations$count) & is.na(counts))) {
        stop(paste(path, ": a count exceeds R's integer range"))
    }

    observations$count <- counts
    return(observations)
}


summarise_observations <- function(data) {
    # Remove exact duplicate rows, rather than duplicate count values.
    unique_data <- unique(data)

    # Keep the site's first-occurrence order.
    sites <- c()
    for (site in unique_data$site) {
        if (!(site %in% sites)) {
            sites <- c(sites, site)
        }
    }

    totals <- numeric(0)
    missing_counts <- integer(0)

    for (site in sites) {
        counts <- unique_data$count[unique_data$site == site]

        total_known <- 0
        missing_count <- 0
        flag <- TRUE

        for (count in counts) {
            if (is.na(count)) {
                missing_count <- missing_count + 1
            } else {
                total_known <- total_known + count
                flag <- FALSE
            }
        }

        # A known zero clears the flag; all-missing counts do not.
        if (flag) {
            total_known <- NA_real_
        }

        totals <- c(totals, total_known)
        missing_counts <- c(missing_counts, missing_count)
    }

    return(data.frame(
        site = as.character(sites),
        total_known = totals,
        missing_count = missing_counts
    ))
}


# Read and inspect the ordinary data.
valid_data <- read_observations("data/bootcamp_observations.csv")
str(valid_data)
print(valid_data)

# Read the boundary data and summarise both files.
boundary_data <- read_observations(
    "data/bootcamp_observations_boundary.csv"
)

valid_summary <- summarise_observations(valid_data)
boundary_summary <- summarise_observations(boundary_data)

print(valid_summary)
print(boundary_summary)

# Check the four site summaries required by the exercise.
stopifnot(
    valid_summary$total_known[valid_summary$site == "A"] == 2,
    valid_summary$missing_count[valid_summary$site == "A"] == 1
)

stopifnot(
    valid_summary$total_known[valid_summary$site == "B"] == 0,
    valid_summary$missing_count[valid_summary$site == "B"] == 0
)

stopifnot(
    is.na(boundary_summary$total_known[boundary_summary$site == "C"]),
    boundary_summary$missing_count[boundary_summary$site == "C"] == 2
)

stopifnot(
    boundary_summary$total_known[boundary_summary$site == "D"] == 0,
    boundary_summary$missing_count[boundary_summary$site == "D"] == 0
)

# Catch the expected invalid-input error without ending the script.
invalid_result <- try(
    read_observations("data/bootcamp_observations_invalid.csv"),
    silent = TRUE
)
stopifnot(class(invalid_result) == "try-error")
print(invalid_result)

# Combine summaries for a base-R figure.
all_summaries <- rbind(valid_summary, boundary_summary)

if (!dir.exists("results")) {
    dir.create("results")
}

pdf("results/observations_known_totals.pdf")

plot(
    1:nrow(all_summaries),
    all_summaries$total_known,
    pch = 19,
    xaxt = "n",
    ylim = c(0, 3),
    xlab = "Site",
    ylab = "Known-count total",
    main = "Known observation totals",
    sub = "Site C: all counts missing; no total or point is shown."
)

axis(
    1,
    at = 1:nrow(all_summaries),
    labels = all_summaries$site
)

dev.off()