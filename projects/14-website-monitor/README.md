# Website Availability Monitor

Monitor website health and response times.

## Features

- HTTP status checking
- Response time measurement
- Configurable timeout
- JSON and CSV export
- Error logging

## Setup

```bash
cd projects/14-website-monitor
python3 -m pip install requests --user
```

## Usage

```bash
cd projects/14-website-monitor/src

# Check single URL
python cli.py https://example.com

# Check multiple URLs
python cli.py https://example.com https://google.com

# Custom timeout
python cli.py https://example.com -t 5

# Export results
python cli.py https://example.com -o results.json
python cli.py https://example.com -o results.csv
```

## Testing

```bash
cd projects/14-website-monitor
python tests/test_monitor.py
```

## Dependencies

- Python 3.11+
- requests

## Ethics

- Respects timeouts
- No aggressive request rates
- For monitoring owned/authorized sites only
