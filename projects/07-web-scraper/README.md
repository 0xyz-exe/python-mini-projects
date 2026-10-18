# Web Scraper

Responsible web scraping with BeautifulSoup.

## Features

- Extract titles, headings, links
- Configurable timeouts and delays
- User-Agent headers
- JSON and CSV export
- Error handling

## Setup

```bash
cd projects/07-web-scraper
python3 -m pip install requests beautifulsoup4 --user
```

## Usage

```bash
cd projects/07-web-scraper/src

# Scrape page
python cli.py https://example.com

# Export to JSON
python cli.py https://example.com -o data.json -f json

# Export to CSV
python cli.py https://example.com -o links.csv -f csv

# Custom timeout and delay
python cli.py https://example.com -t 20 -d 2.0
```

## Testing

```bash
cd projects/07-web-scraper
python tests/test_scraper.py
```

## Dependencies

- Python 3.11+
- requests
- beautifulsoup4

## Ethics

- Respects timeouts
- Uses delays between requests
- Identifies as educational scraper
- Does not bypass authentication
