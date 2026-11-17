"""
Application execution entry point.

This module serves as the primary entry point for the sales report 
pipeline, orchestrating file input, data cleaning, metric summarization, 
and report generation when executed from the command line.
"""

from .file_io import run_report
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
# gets the project root

input_path = PROJECT_ROOT / "data" / "orders.csv"
output_path = PROJECT_ROOT / "output" / "summary_of_orders.json"

def main() -> None:
    """
    Execute the main order processing pipeline.

    Triggers the end-to-end report generation process using the default 
    input orders file and output summary destination.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    run_report(input_path, output_path)

if __name__ == "__main__":
    main()