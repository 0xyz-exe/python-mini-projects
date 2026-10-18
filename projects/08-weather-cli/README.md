# Weather CLI

Command-line weather application using Open-Meteo API.

## Features

- Current weather by coordinates
- Free API (no key required)
- Offline demo mode with sample data
- Timeout handling
- JSON sample responses

## Setup

```bash
cd projects/08-weather-cli
python3 -m pip install requests --user
```

## Usage

```bash
cd projects/08-weather-cli/src

# Get weather (Bangkok coordinates)
python cli.py --lat 13.7563 --lon 100.5018

# Demo mode (offline sample)
python cli.py --demo

# Save sample response
python cli.py --save-sample sample.json
```

## Testing

```bash
cd projects/08-weather-cli
python tests/test_weather.py
```

## Dependencies

- Python 3.11+
- requests

## API

Uses Open-Meteo (https://open-meteo.com) - free, no authentication required.
