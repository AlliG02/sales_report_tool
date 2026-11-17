"""
Order data validation and normalization.

This module provides functions to sanitize, validate, and convert raw CSV order 
fields (such as IDs, statuses, quantities, prices, and dates) into clean, 
standardized formats ready for downstream reporting.
"""

from datetime import date
from typing import Any

def normalise_order_id(order_id: str | None) -> str | None:
    """
    Normalize and validate an order ID string.

    Strips leading and trailing whitespace. Returns None if the ID is 
    empty, blank, or null.

    Args:
        order_id (str | None): The raw order ID to normalize.

    Returns:
        str | None: The stripped order ID, or None if invalid.
    """
    if order_id is None:
        return None
    stripped = order_id.strip()
    return stripped if stripped else None

def normalise_status(status: str | None) -> str | None:
    """
    Normalize and validate an order status.

    Cleans whitespace, converts to lowercase, and checks against 
    the allowed set of statuses ('paid', 'refunded', 'pending').

    Args:
        status (str | None): The raw status string to normalize.

    Returns:
        str | None: The normalized status if allowed, or None if invalid.
    """
    if status is None:
        return None

    normalised = status.strip().lower()
    allowed_statuses = {"paid", "refunded", "pending"}
    return normalised if normalised in allowed_statuses else None

def normalise_quantity(quantity: str | int | None) -> int | None:
    """
    Parse and validate an item quantity.

    Converts the input to an integer and ensures it is strictly greater than zero.

    Args:
        quantity (str | int | None): The raw quantity value to parse.

    Returns:
        int | None: The positive integer quantity, or None if parsing fails or value <= 0.
    """
    try:
        parsed = int(quantity)  # type: ignore
    except (ValueError, TypeError):
        return None

    return parsed if parsed > 0 else None

def normalise_unit_price(unit_price: str | float | None) -> float | None:
    """
    Parse and validate a unit price.

    Converts the input to a float and ensures it is strictly greater than zero.

    Args:
        unit_price (str | float | None): The raw unit price value to parse.

    Returns:
        float | None: The positive float price, or None if parsing fails or value <= 0.
    """
    try:
        parsed = float(unit_price)  # type: ignore
    except (ValueError, TypeError):
        return None

    return parsed if parsed > 0 else None

def normalise_order_date(order_date: str | None) -> str | None:
    """
    Parse and validate an order date into ISO 8601 format.

    Attempts to parse the input date string and return its ISO format representation.

    Args:
        order_date (str | None): The raw date string to validate.

    Returns:
        str | None: The ISO-formatted date string, or None if parsing fails.
    """
    try:
        return date.fromisoformat(order_date).isoformat()  # type: ignore
    except (TypeError, ValueError) as e:
        print(f"Invalid date: {e}")
        return None

def clean_order(raw_order: dict[str, Any]) -> dict[str, Any] | None:
    """
    Transform and validate a raw order dictionary into a clean record.

    Extracts fields from the raw order dictionary, normalizes each value 
    individually, and returns a fully validated clean dictionary if all fields 
    pass validation; otherwise, returns None.

    Args:
        raw_order (dict[str, Any]): A dictionary containing raw order attributes.

    Returns:
        dict[str, Any] | None: A dictionary of cleaned and validated order data, 
        or None if any validation check fails.
    """
    valid = True

    order_id = raw_order.get("order_id")
    status = raw_order.get("status")
    quantity = raw_order.get("quantity")
    unit_price = raw_order.get("unit_price")
    order_date = raw_order.get("order_date")

    normalised_order_id = normalise_order_id(order_id)
    if normalised_order_id is None:
        valid = False

    normalised_status = normalise_status(status)
    if normalised_status is None:
        valid = False

    normalised_quantity = normalise_quantity(quantity)
    if normalised_quantity is None:
        valid = False

    normalised_unit_price = normalise_unit_price(unit_price)
    if normalised_unit_price is None:
        valid = False

    normalised_date = normalise_order_date(order_date)
    if normalised_date is None:
        valid = False

    cleaned = {
        "order_id": normalised_order_id,
        "status": normalised_status,
        "quantity": normalised_quantity,
        "unit_price": normalised_unit_price,
        "order_date": normalised_date
    }

    if valid:
        return cleaned
    else:
        return None