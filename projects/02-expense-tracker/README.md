# Expense Tracker

Personal finance tracker with categories and summaries.

## Features

- Track income and expenses
- Categories and descriptions
- Monthly summaries
- Category breakdowns
- CSV import/export
- JSON persistence

## Usage

```bash
cd projects/02-expense-tracker/src

# Add income
python cli.py add income 1000 Salary -d "Monthly salary"

# Add expense
python cli.py add expense 50 Food -d "Lunch" --date 2026-10-15

# List all
python cli.py list

# Monthly summary
python cli.py monthly 2026 10

# Category breakdown
python cli.py categories

# Export to CSV
python cli.py export transactions.csv

# Import from CSV
python cli.py import transactions.csv
```

## Testing

```bash
cd projects/02-expense-tracker
python tests/test_expense_tracker.py
```

## Dependencies

Python 3.11+ (stdlib only)
