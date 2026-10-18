# CSV Data Analyzer

Analyze and clean CSV data.

## Features

- Load and inspect CSV
- Missing value detection
- Numeric statistics (min, max, mean, median)
- Group by and count
- Export cleaned data
- Sample dataset included

## Usage

```bash
cd projects/11-csv-data-analyzer/src

# Summary
python cli.py data.csv summary

# Missing values
python cli.py data.csv missing

# Numeric stats
python cli.py data.csv stats age

# Group by
python cli.py data.csv group category

# Export cleaned
python cli.py data.csv clean output.csv
```

## Sample Data

```csv
name,age,city
Alice,30,NYC
Bob,25,LA
Charlie,35,Chicago
```

## Testing

```bash
cd projects/11-csv-data-analyzer
python tests/test_csv_analyzer.py
```

## Dependencies

Python 3.11+ (stdlib only)
