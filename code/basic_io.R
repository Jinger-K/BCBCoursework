# A simple R script illustrating file input and output.
# Run from the coursework project root with:
# Rscript code/basic_io.R

MyData <- read.csv("data/trees.csv", header = TRUE) # Import with headers

write.csv(MyData, "results/MyData.csv") # Write it as a new file

write.table(MyData[1, ], file = "results/MyData,csv", append = TRUE)

write.csv(MyData, "results/MyData.csv", row.names = TRUE)

write.table(MyData, "results/MyData.csv", col.names = FALSE) # Omit column names

print("Script complete!")
