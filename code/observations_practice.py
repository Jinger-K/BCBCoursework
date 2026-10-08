import csv


def load_observations(path): # ffunction to read csv file
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def parse_count(count_text): #function to interpret data input
    
    if not isinstance(count_text,str):
        raise ValueError("Count must be text")

    if count_text == "":
        return None
    
    count_text = int(count_text)

    if count_text < 0:
        raise ValueError("Count cannot be negative")

    return count_text
    

# write summarise_site(rows, site)
# INPUT: observations with site, date and count
# Check that the expected fields are present; stop and report an error if not
# Identify exact duplicate records
# Keep one copy of each record (site, date, count), including missing counts
# For each site: report how many couts are missing
#   if at least one count is present:
#       add the count that are present and report the known-count total
#   Otherwise:
#       report that no known total is available
# OUTPUT: (known_total, missing_count) known-count total (or unavailable) and missing-count number per site


def summarise_site(rows, site):
    unique = []
    
    # validate all rows and remove duplicates
    for row in rows:
        # Check that all required fields are present
        if "site" not in row:
            raise ValueError("Missing site")
        if "date" not in row:
            raise ValueError("Missing date")
        if "count" not in row:
            raise ValueError("Missing count")
        
        # Check that there are no extra fields
        if len(row) != 3:
            raise ValueError("Row has extra fields")
        
        # Check site
        if type(row["site"]) != str:
            raise ValueError("Site must be text")
        if row["site"] == "":
            raise ValueError("Site cannot be empty")
        # Check date
        if type(row["date"]) != str:
            raise ValueError("Date must be text")
        if row["date"] == "":
            raise ValueError("Date cannot be empty")
        # Check count
        if type(row["count"]) != str:
            raise ValueError("Count must be text")
           
        # Validate count
        parse_count(row["count"])

        # Keep only one copy of an exact duplicate
        if row not in unique:
            unique.append(row)
    
    #Prepare for counting
    known_total = 0
    missing_count = 0
    known_test = 0

    for row in unique:
        if row["site"] == site: # Summarise only the requested site
            count = parse_count(row["count"])
            if count == None:
                missing_count += 1
            else:
                known_total += count
                known_test += 1
        
    # If no known observation
    if known_test == 0:
        known_total = None

    return (known_total, missing_count)


if __name__ == "__main__":
    rows = load_observations("data/bootcamp_observations.csv")
    print(rows[0])
    print(rows[2])