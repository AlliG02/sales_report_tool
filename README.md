Purpose: validate CSV orders and generate a JSON sales summary.
Rules: only valid paid orders contribute to revenue and units sold.
Setup: create a virtual environment and install requirements-dev.txt.
Tests: run python -m pytest -v.

## Run the report

From the project root, with your virtual environment activated:

```bash
cd src
python3 -m sales_report.main
cd ..
```

Reads `data/orders.csv` and writes `output/summary_of_orders.json`.
