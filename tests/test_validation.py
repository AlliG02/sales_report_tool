import pytest
from sales_report.validation import clean_order

# way of injecting the same test date into several tests
@pytest.fixture
def valid_order():
    return {
        "order_id": "ORD-001",
        "status": "paid",
        "quantity": "2",
        "unit_price": "5.00",
        "order_date": "2026-11-01",
    }

# follows the AAA pattern: Arrange, Act, Assert
def test_clean_order_normalises_valid_order(valid_order):
    result = clean_order(valid_order)

    assert result == {
        "order_id": "ORD-001",
        "status": "paid",
        "quantity": 2,
        "unit_price": 5.0,
        "order_date": "2026-11-01",
    }

def test_clean_order_rejects_missing_fields():
    assert clean_order({}) is None

def test_clean_order_rejects_negative_price(valid_order):
    valid_order["unit_price"] = -5
    assert clean_order(valid_order) is None

# decorator example
@pytest.mark.parametrize("price", ["-5.00", "0", "", "bad", None])
def test_clean_order_rejects_invalid_price(valid_order, price):
    valid_order["unit_price"] = price
    assert clean_order(valid_order) is None

# decorators allow us to test for multiple different values
# this allows us to avoid writing multiple different test cases 
# we can reuse the same test case for different values
@pytest.mark.parametrize("quantity", ["0", "-2", "bad", "1.5", None])
def test_clean_order_rejects_invalid_quantities(valid_order, quantity):
    valid_order["quantity"] = quantity
    assert clean_order(valid_order) is None

@pytest.mark.parametrize("invalid_date", ["2026-02-30", "not-a-date", "", None])
def test_clean_order_rejects_invalid_dates(valid_order, invalid_date):
    valid_order["order_date"] = invalid_date
    assert clean_order(valid_order) is None

def test_clean_order_does_not_modify_input(valid_order):
    original = valid_order.copy()
    clean_order(valid_order)
    assert valid_order == original