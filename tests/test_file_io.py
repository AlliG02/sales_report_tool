import json
from sales_report.file_io import run_report

def test_run_report_returns_false_when_input_missing(tmp_path):
    input_path = tmp_path / "missing.csv"
    output_path = tmp_path / "summary_of_orders.json"
    assert run_report(input_path, output_path) is False
    assert not output_path.exists()

def test_run_report_writes_summary(tmp_path):
    input_path = tmp_path / "orders.csv"
    output_path = tmp_path / "summary.json"

    input_path.write_text(
        "order_id,status,quantity,unit_price,order_date\n"
        "001,paid,2,10.00,2026-11-01\n",
        encoding="utf-8",
    )
    assert run_report(input_path, output_path) is True
    result = json.loads(output_path.read_text(encoding="utf-8"))
    expected = {
        "rows_read": 1,
        "valid_orders": 1,
        "rejected_orders": 0,
        "paid_orders": 1,
        "units_sold": 2,
        "revenue": 20.0
    }
    assert expected == result