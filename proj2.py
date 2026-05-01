import csv
import math
from dataclasses import dataclass
from typing import *
import sys
sys.setrecursionlimit(10_000)

# Put your data definitions first!

# ...

# Then your functions.

@dataclass(frozen=True)
class Row:
    country : str
    year : int
    # floats or None
    electricity_and_heat_co2_emissions : Optional[float]
    electricity_and_heat_co2_emissions_per_capita : Optional[float]
    energy_co2_emissions : Optional[float]
    energy_co2_emissions_per_capita : Optional[float]
    total_co2_emissions_excluding_lucf : Optional[float]
    total_co2_emissions_excluding_lucf_per_capita : Optional[float]

@dataclass(frozen=True)
class Node:
    value : Row
    next : Optional['Node']

def str_to_float(s: str) -> Optional[float]:
            """Helper to convert empty strings to None, or valid strings to float."""
            if s == "":
                return None
            else:
                return float(s)

def parse_row(fields: list[str]) -> Row:
    """Takes a list of 8 strings and converts them into a Row object."""
    country = fields[0]
    year = int(fields[1])

    electricity_and_heat_co2_emissions = str_to_float(fields[2])
    electricity_and_heat_co2_emissions_per_capita = str_to_float(fields[3])
    energy_co2_emissions = str_to_float(fields[4])
    energy_co2_emissions_per_capita = str_to_float(fields[5])
    total_co2_emissions_excluding_lucf = str_to_float(fields[6])
    total_co2_emissions_excluding_lucf_per_capita = str_to_float(fields[7])

    return Row(
        country=country,
        year=year,
        electricity_and_heat_co2_emissions=electricity_and_heat_co2_emissions,
        electricity_and_heat_co2_emissions_per_capita=electricity_and_heat_co2_emissions_per_capita,
        energy_co2_emissions=energy_co2_emissions,
        energy_co2_emissions_per_capita=energy_co2_emissions_per_capita,
        total_co2_emissions_excluding_lucf=total_co2_emissions_excluding_lucf,
        total_co2_emissions_excluding_lucf_per_capita=total_co2_emissions_excluding_lucf_per_capita
    )

def build_linked_list_helper(raw_rows: list[list[str]]) -> Optional[Node]:
    # 1. BASE CASE
    # If there are no more rows left in our list, we've reached the end!
    if len(raw_rows) == 0:
        return None
    
    # 2. RECURSIVE STEP
    # Grab the very first list of strings from our pile
    first_row_strings = raw_rows[0]
    
    # Use the parse_row function you already wrote to turn those strings into a Row box
    current_row_object = parse_row(first_row_strings)
    
    # Now, we create the Node. 
    # To fill in the 'next' part, we call THIS function again with the rest of the rows!
    return Node(
        value=current_row_object,
        next=build_linked_list_helper(raw_rows[1:]) 
    )


def read_csv_lines(filename: str) -> Optional[Node]:
    """reads csv"""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
    
        remaining_rows = list(reader)

    return build_linked_list_helper(remaining_rows)
