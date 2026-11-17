"""
Order reporting and metric calculations.

This module provides functionality to aggregate raw order data, separate
valid records from rejections, and compute business metrics such as 
units sold and total revenue.
"""

from .validation import clean_order

def summarise_rows(raw_data: list[dict]) -> dict:
    """
    Summarize a collection of raw order dictionaries and calculate key metrics.

    Passes raw orders through the validation cleaner, separates valid and 
    rejected entries, and aggregates statistics specifically for paid orders.

    Args:
        raw_data (list[dict]): A list of raw order dictionaries to process.

    Returns:
        dict: A summary report containing aggregated business metrics:
            - rows_read (int): Total number of rows processed.
            - valid_orders (int): Number of successfully validated orders.
            - rejected_orders (int): Number of failed or discarded orders.
            - paid_orders (int): Number of valid orders with a 'paid' status.
            - units_sold (int): Total quantity of items sold in paid orders.
            - revenue (float): Total calculated revenue rounded to 2 decimal places.
    """
    cleaned_data = [clean_order(row) for row in raw_data] 
    rejected = [row for row in cleaned_data if row is None]
    valid = [row for row in cleaned_data if row is not None]
    valid_paid = [row for row in valid if row["status"] == "paid"]
    units_sold = sum(row["quantity"] for row in valid_paid)
    revenue = sum(row["quantity"] * row["unit_price"] for row in valid_paid)

    report = {
        "rows_read": len(raw_data),
        "valid_orders": len(valid),
        "rejected_orders": len(rejected),
        "paid_orders": len(valid_paid),
        "units_sold": units_sold,
        "revenue": round(revenue, 2)
    }

    return report