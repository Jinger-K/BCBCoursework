#!/usr/bin/env python3
"""Validate and clean the synthetic Silwood tree survey."""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "silwood_trees_raw.csv"
RESULTS_DIR = PROJECT_ROOT / "results"

INPUT_FIELDS = [
    "record_id",
    "location",
    "genus",
    "species",
    "distance_m",
    "angle_degrees",
]
ISSUE_FIELDS = ["source_row", "record_id", "reasons"]
OAK_COUNT_FIELDS = ["species", "count"]


def load_records(path: Path = INPUT_PATH) -> list[dict[str, str]]:
    """Load survey records and check that the published columns are present."""
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != INPUT_FIELDS:
            raise ValueError(
                f"Expected columns {INPUT_FIELDS}, found {reader.fieldnames}"
            )
        return list(reader)


def validate_record(
    row: dict[str, str],
    source_row: int,
    accepted_ids: set[str],
) -> tuple[dict[str, str] | None, list[str]]:
    """Return a cleaned record or its ordered rejection reasons."""

    reasons = [] # Create an empty list to store errors

    # Check record_id
    record_id = row["record_id"].strip() # Remove surrounding whitespace

    if record_id == "":
        reasons.append("missing record_id") # Report missing record
    else: # Check validity of existing record
        flag = True
        if len(record_id) != 5 or record_id[:2] != "ST":
            flag = False
        for character in record_id[2:]:
            if character not in "0123456789":
                flag = False
        if flag == False:
            reasons.append("invalid record_id")
        # Check if it's duplicated
        if record_id in accepted_ids:
            reasons.append("duplicate record_id")
    
    # Check location
    valid_locations = [ "Silwood Bottom", "Nash's Field", "Manor House", "Reactor Wood" ]

    location = row["location"].strip() # Remove surrounding whitespace

    if location == "":
        reasons.append("missing location")
    else:
        location_found = False
        for valid_location in valid_locations:
            if location.lower() == valid_location.lower():
                location_found = True
                location = valid_location
        if location_found == False:
            reasons.append("invalid location")

    # Check genus
    valid_genera = ["Quercus", "Acer", "Betula", "Fagus", "Fraxinus"]

    genus = row["genus"].strip()
    genus_found = False # Define out of the conditions to help verifications later on

    if genus == "":
        reasons.append("missing genus")
    else:
        for valid_genus in valid_genera:
            if genus.lower() == valid_genus.lower():
                genus_found = True
                genus = valid_genus

        if genus_found == False:
            reasons.append("invalid genus")

    # Check species
    valid_species_names = ["robur", "petraea", "pseudoplatanus", "pendula", "sylvatica", "excelsior",]

    species = row["species"].strip()
    species_found = False

    if species == "":
        reasons.append("missing species")
    else:
        for valid_species in valid_species_names:
            if species.lower() == valid_species.lower():
                species_found = True
                species = valid_species

        if species_found == False:
            reasons.append("invalid species")

    # Check genus and species pair
    valid_pairs = [
        ("Quercus", "robur"),
        ("Quercus", "petraea"),
        ("Acer", "pseudoplatanus"),
        ("Betula", "pendula"),
        ("Fagus", "sylvatica"),
        ("Fraxinus", "excelsior"),
    ]

    if genus_found and species_found:
        if (genus, species) not in valid_pairs:
            reasons.append("invalid genus/species combination")

    
    # Check distance
    distance = row["distance_m"].strip()

    if distance == "":
        reasons.append("missing distance_m")
    else:
        try:
            distance = float(distance)
        except ValueError:   # In case invalid characters interrupt the process
            reasons.append("invalid distance_m")
        else:
            if not math.isfinite(distance):
                reasons.append("invalid distance_m")
            elif distance <= 0 or distance > 100:
                reasons.append("distance_m out of range")
                
    # Check angle
    angle = row["angle_degrees"].strip()

    if angle == "":
        reasons.append("missing angle_degrees")
    else:
        try:
            angle = float(angle)
        except ValueError:
            reasons.append("invalid angle_degrees")
        else:
            if not math.isfinite(angle):
                reasons.append("invalid angle_degrees")
            elif angle <= 0 or angle >= 90:
                reasons.append("angle_degrees out of range")
    
    # Return validation results
    if len(reasons) > 0:
        return None, reasons
    else:
        cleaned_record = {
            "record_id": record_id,
            "location": location,
            "genus": genus,
            "species": species,
            "distance_m": str(distance),
            "angle_degrees": str(angle),
        }

        return cleaned_record, reasons



def process_records(
    rows: Iterable[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Separate accepted records from rejected-row reports."""
    cleaned_records = []
    error_log = []
    accepted_ids = set()

    source_row = 2 # Initialise source row

    for row in rows:
        cleaned_record, reasons = validate_record(row, source_row, accepted_ids)
        
        if cleaned_record is not None:
            cleaned_records.append(cleaned_record)
            accepted_ids.add(cleaned_record["record_id"])
        else:
            reasons_temp = ""

            for reason in reasons:
                reasons_temp = reasons_temp + reason + "; "

            reasons_temp = reasons_temp[:-2] # Exclude final "; "

            issue = {
                "source_row": str(source_row),
                "record_id": row["record_id"].strip(),
                "reasons": reasons_temp
            }

            error_log.append(issue)
            
        
        source_row = source_row + 1

    # Sort the cleaned data
    # Sort the accepted identifiers
    sorted_ids = sorted(accepted_ids)

    #Arrange the complete records in identifier order
    sorted_records = []

    for record_id in sorted_ids:
        for record in cleaned_records:
            if record["record_id"] == record_id:
                sorted_records.append(record)

    return sorted_records, error_log



def summarise_oaks(clean_records: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Count accepted oak records by species."""
    counts = {}
    for record in clean_records:
        if record["genus"] == "Quercus":
            species = record["species"]
            if species not in counts:
                counts[species] = 0
            counts[species] += 1
    
    oak_counts = []
    sorted_counts = sorted(counts)
    for species in sorted_counts:
        species_count = {
            "species":species,
            "count":str(counts[species])
        }
        oak_counts.append(species_count)
    return oak_counts


def write_csv(
    path: Path,
    fieldnames: list[str],
    rows: Iterable[dict[str, str]],
) -> None:
    """Replace a CSV file with the supplied rows."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Run the complete validation workflow."""
    clean_records, issues = process_records(load_records())
    oak_counts = summarise_oaks(clean_records)

    write_csv(
        RESULTS_DIR / "silwood_trees_clean.csv",
        INPUT_FIELDS,
        clean_records,
    )
    write_csv(
        RESULTS_DIR / "silwood_tree_issues.csv",
        ISSUE_FIELDS,
        issues,
    )
    write_csv(
        RESULTS_DIR / "oak_species_counts.csv",
        OAK_COUNT_FIELDS,
        oak_counts,
    )


if __name__ == "__main__":
    main()
