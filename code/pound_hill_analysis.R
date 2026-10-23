# Run from the project root:
# Rscript code/pound_hill_analysis.R
library(reshape2)
library(dplyr)
library(ggplot2)

# Read the raw data.
# The first row contains treatment information, so it is not a header.
RawData <- read.csv("data/pound_hill_data.csv", header = FALSE)

# Read the metadata, which has a header and uses semicolons.
MetaData <- read.csv("data/pound_hill_meta_data.csv",
                     header = TRUE, sep = ";")

# Inspect the dimensions, column types and first six rows.
dim(RawData)
str(RawData)
head(RawData)

dim(MetaData)
str(MetaData)
head(MetaData)

# Transpose the data
TData <- t(as.matrix(RawData))

# Remove the first row and convert the remaining data to a data frame
TempData <- as.data.frame(TData[-1, ])
colnames(TempData) <- TData[1, ]

# Replace blank species counts with zeros
SpeciesCounts <- TempData[, -(1:4)] # The first four columns are sampling labels
SpeciesCounts[is.na(SpeciesCounts) | SpeciesCounts == ""] <- 0
TempData[, -(1:4)] <- SpeciesCounts

# Convert to longdata
LongData <- reshape2::melt(
    TempData, 
    id.vars = c("Cultivation", "Block", "Plot", "Quadrat"), 
    variable.name = "Species", 
    value.name = "Count")
LongData$Count <- as.numeric(LongData$Count)

head(LongData)
str(LongData)
dim(LongData)

# Check the validity of count
# Stop if counts are not numeric.
if (!is.numeric(LongData$Count)) {
    stop("Counts must be numeric.")
}

# Stop if counts contain missing values.
if (any(is.na(LongData$Count))) {
    stop("Counts contain missing values.")
}

# Stop if counts contain negative values.
if (any(LongData$Count < 0)) {
    stop("Counts cannot be negative.")
}

# Create empty character vectors to store distinct labels.
SpeciesSeen <- character(0)
QuadratsSeen <- character(0)
PlotsSeen <- character(0)

# Examine each row.
for (i in 1:nrow(LongData)) {

    # Convert the species label from a factor to text.
    SpeciesName <- as.character(LongData$Species[i])

    # Identify each quadrat using all four sampling labels.
    QuadratID <- paste(
        LongData$Cultivation[i],
        LongData$Block[i],
        LongData$Plot[i],
        LongData$Quadrat[i],
        sep = "_"
    )

    # Identify each plot using its treatment, block and plot labels.
    PlotID <- paste(
        LongData$Cultivation[i],
        LongData$Block[i],
        LongData$Plot[i],
        sep = "_"
    )

    # Record each species only once.
    if (!(SpeciesName %in% SpeciesSeen)) {
        SpeciesSeen <- c(SpeciesSeen, SpeciesName)
    }

    # Record each quadrat only once.
    if (!(QuadratID %in% QuadratsSeen)) {
        QuadratsSeen <- c(QuadratsSeen, QuadratID)
    }

    # Record each plot only once.
    if (!(PlotID %in% PlotsSeen)) {
        PlotsSeen <- c(PlotsSeen, PlotID)
    }
}

# Print the numbers of distinct species, quadrats and plots.
print(paste("Number of species:", length(SpeciesSeen)))
print(paste("Number of quadrats:", length(QuadratsSeen)))
print(paste("Number of plots:", length(PlotsSeen)))

# Calculate species richness for each quadrat.
QuadratGroups <- group_by(
    LongData,
    Cultivation, Block, Plot, Quadrat
)

QuadratRichness <- summarise(
    QuadratGroups,
    Richness = sum(Count > 0)
)

PlotGroups <- group_by(
    QuadratRichness,
    Cultivation, Block, Plot
)

PlotRichness <- summarise(
    PlotGroups,
    MeanRichness = mean(Richness)
)

head(PlotRichness)
dim(PlotRichness)
table(PlotRichness$Plot)

# Create the results directory if it does not already exist.
dir.create("results", showWarnings = FALSE)

# Save data
write.csv(
    PlotRichness,
    "results/pound_hill_plot_richness.csv",
    row.names = FALSE
)

# Plot the figure
# Plot each plot-level mean
RichnessFigure <- ggplot(
    PlotRichness,
    aes(
        x = Cultivation,
        y = MeanRichness,
        colour = Block
    )
) +
    geom_point(size = 3, shape = 16) +
    labs(
        x = "Cultivation month",
        y = "Mean number of plant species per quadrat",
        colour = "Block"
    ) +
    theme_bw(base_size = 12)

# print(RichnessFigure)

# Save the figure.
ggsave(
    "results/pound_hill_plot_richness.pdf",
    plot = RichnessFigure,
    width = 7,
    height = 5
)

# May cultivation shows the highest typical richness, and richness varies within all three treatments, and the values overlap between treatments.
# The figure alone does not establish causation.
# To assess whether cultivation timing caused these differences, we would
# need to know treatments were randomly allocated or not,
# plots were independent, other management and conditions were comparable, etc..


# Repeat the plot-lvel summary for total abundance
# Calculate total abundance in each quadrat.
QuadratAbundance <- summarise(
    QuadratGroups,
    Abundance = sum(Count)
)

# Group quadrats by plot.
AbundancePlotGroups <- group_by(
    QuadratAbundance,
    Cultivation, Block, Plot
)

# Calculate mean quadrat abundance for each plot.
PlotAbundance <- summarise(
    AbundancePlotGroups,
    MeanAbundance = mean(Abundance)
)

dim(PlotAbundance)
print(PlotAbundance)

# October generally shows higher plot-level mean abundance, whereas May
# shows the highest typical species richness.
# Abundance counts individuals, whereas richness counts species, so having
# more individuals does not necessarily mean having more species.