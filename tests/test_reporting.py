from sales_report.reporting import summarise_rows

def test_summarise_rows_with_empty_input():
    expected = {
        "rows_read": 0,
        "valid_orders": 0,
        "rejected_orders": 0,
        "paid_orders": 0,
        "units_sold": 0,
        "revenue": 0,
    }
    assert summarise_rows([]) == expected

def test_summarised_rows_with_mixed_orders():
    rows = [
        {"order_id": "001", "status": "paid", "quantity": "2",
        "unit_price": "10.00", "order_date": "2026-11-01"},
        {"order_id": "002", "status": "pending", "quantity": "3",
        "unit_price": "5.00", "order_date": "2026-11-01"},
        {"order_id": "003", "status": "refunded", "quantity": "1",
        "unit_price": "12.00", "order_date": "2026-11-01"},
        {"order_id": "004", "status": "paid", "quantity": "bad",
        "unit_price": "8.00", "order_date": "2026-11-01"},
    ]
    expected = {
        "rows_read": 4,
        "valid_orders": 3,
        "rejected_orders": 1,
        "paid_orders": 1,
        "units_sold": 2,
        "revenue": 20.0
    }
    assert summarise_rows(rows) == expected