# Sales Report Tool

A lightweight Python utility designed to validate raw sales CSV exports, filter valid transactions, and generate a structured JSON sales summary.

---

## 🛠️ Project Setup & Installation

Before running the tool or tests, make sure your virtual environment is active and dependencies are installed.

1. **Create and activate your virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

2. **Install development requirements:**
   ```bash
   pip install -r requirements-dev.txt
   ```

---

## 🧪 Running Tests

This project uses `pytest` for data-driven and unit testing. To run the test suite, execute:

```bash
python -m pytest -v
```

---

## 🚀 Running the Report

The script reads raw order records, validates formatting, computes revenue metrics, and outputs a clean JSON summary.

From the project root (with your virtual environment activated), run:

```bash
cd src
python3 -m sales_report.main
cd ..
```

* **Input:** `data/orders.csv`
* **Output:** `output/summary_of_orders.json`

---

## 📊 Business Rules

* Only **valid, paid orders** contribute directly to total revenue and units sold.
* Malformed rows, negative pricing, or missing values are caught and handled during the validation and cleaning pipeline.