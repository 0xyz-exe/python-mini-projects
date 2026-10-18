# Text and Log Analyzer

Analyze text files and application logs.

## Features

- Count words, lines, characters
- Frequent term analysis
- Log severity level analysis
- Filter logs by keyword or date
- JSON and CSV export

## Usage

```bash
cd projects/05-text-log-analyzer/src

# Basic statistics
python cli.py myfile.txt stats

# Top 10 frequent words
python cli.py myfile.txt frequent -n 10

# Log severity analysis
python cli.py app.log logs

# Filter logs
python cli.py app.log filter -k ERROR
python cli.py app.log filter -d 2026-10-18

# Export report
python cli.py myfile.txt export report.json -f json
```

## Testing

```bash
cd projects/05-text-log-analyzer
python tests/test_text_analyzer.py
```

## Dependencies

Python 3.11+ (stdlib only)
