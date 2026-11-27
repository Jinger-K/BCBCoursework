# A simple R script illustrating file input and output.
# Run from the coursework project root with:
# Rscript code/basic_io.R

MyData <- read.csv("data/trees.csv", header = TRUE)

# Create the output directory if it does not already exist.
if (!dir.exists("results")) {
    dir.create("results")
}

# Write the full dataset, including row names by default.
write.csv(MyData, "results/MyData.csv")

# Append the first row; appending column names produces an expected warning.
write.table(MyData[1, ], file = "results/MyData.csv", append = TRUE)

# Overwrite the file, explicitly including row names.
write.csv(MyData, "results/MyData.csv", row.names = TRUE)

# Overwrite again without column names; write.table uses spaces by default.
write.table(MyData, "results/MyData.csv", col.names = FALSE)

print("Script complete!")