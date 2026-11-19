"""
Application execution entry point.

This module serves as the primary entry point for the sales report 
pipeline, orchestrating file input, data cleaning, metric summarization, 
and report generation when executed from the command line.
"""

from .file_io import run_report
from pathlib import Path
import argparse

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
# gets the project root

def build_parser() -> argparse.ArgumentParser:
    """
    Specify input and output files from the command line.
    """
    parser = argparse.ArgumentParser(
        description="Generate a sales summary report from an input order dataset."
    )
    parser.add_argument("--input", type=Path, required=True, help="Source sales input file")
    parser.add_argument("--output", type=Path, default="summary_of_orders.json", help="Source sales output file")

    return parser

def main(argv : list[str] | None = None) -> int:
    """
    Execute the main order processing pipeline.

    Triggers the end-to-end report generation process using the default 
    input orders file and output summary destination.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    input_path = PROJECT_ROOT / "data" / args.input
    output_path = PROJECT_ROOT / "output" / args.output
    
    output_path.parent.mkdir(parents=True, exist_ok=True)

    success = run_report(input_path,output_path)

    return 0 if success else 1
    
if __name__ == "__main__":
    raise SystemExit(main())