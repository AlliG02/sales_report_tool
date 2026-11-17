"""
File input and output operations.

This module handles reading raw order data from CSV files and serializing
summarized report dictionaries into JSON output files.
"""

import csv
import json
import logging
from .reporting import summarise_rows


def get_rows_from_csv(filename: str) -> list[dict[str, str]]:
    """
    Read rows from a CSV file into a list of dictionaries.

    Opens the specified CSV file with UTF-8 encoding and uses a DictReader
    to map CSV rows to key-value dictionaries.

    Args:
        filename (str): The path to the CSV file to read.

    Returns:
        list[dict[str, str]]: A list where each row is represented as a dictionary 
        mapping column headers to string values.
    """
    with open(filename, "r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def run_report(input_filename: str, output_filename: str) -> bool:
    """
    Execute the end-to-end report generation pipeline.

    Loads raw order data from an input CSV file, passes it through the reporting 
    summarizer, and writes the resulting metrics dictionary to a JSON file.

    Args:
        input_filename (str): The path to the input CSV file containing raw orders.
        outputfilename (str): The destination path for the JSON summary report.

    Returns:
        bool: True if the report is successfully generated and saved, 
        or False if an error occurs during reading or writing.
    """
    # Get data from CSV
    try:
        raw_data = get_rows_from_csv(input_filename)
    except FileNotFoundError as e:
        print(f"Problem loading input file: {e}")
        return False

    summary = summarise_rows(raw_data)

    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=4)
        return True
    except FileNotFoundError as e:
        logging.error(f"Problem saving to output file: {e}")
        return False