#!/usr/bin/env python3
"""Web Scraper - CLI."""
import argparse
from pathlib import Path
from scraper import WebScraper


def main():
    parser = argparse.ArgumentParser(description="Web scraper")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-f", "--format", choices=["json", "csv"], default="json")
    parser.add_argument("-t", "--timeout", type=int, default=10)
    parser.add_argument("-d", "--delay", type=float, default=1.0)
    
    args = parser.parse_args()
    
    try:
        scraper = WebScraper(timeout=args.timeout, delay=args.delay)
        print(f"Scraping {args.url}...")
        
        data = scraper.scrape(args.url)
        
        print(f"Title: {data['title']}")
        print(f"Headings: {len(data['headings'])}")
        print(f"Links: {len(data['links'])}")
        
        if args.output:
            output_path = Path(args.output)
            if args.format == "json":
                scraper.export_json(data, output_path)
            else:
                scraper.export_csv(data, output_path)
            print(f"✓ Exported to {args.output}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
