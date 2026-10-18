#!/usr/bin/env python3
"""Website Monitor CLI."""
import argparse
from pathlib import Path
from monitor import WebsiteMonitor


def main():
    parser = argparse.ArgumentParser(description="Monitor website availability")
    parser.add_argument("urls", nargs="+", help="URLs to monitor")
    parser.add_argument("-t", "--timeout", type=int, default=10)
    parser.add_argument("-o", "--output", help="Export to file (json or csv)")
    
    args = parser.parse_args()
    
    try:
        monitor = WebsiteMonitor(args.urls, timeout=args.timeout)
        print(f"Checking {len(args.urls)} URLs...")
        
        results = monitor.check()
        
        for url, result in results.items():
            status = "✓" if result['success'] else "✗"
            code = result['status_code'] or "ERR"
            time_ms = result['response_time'] * 1000
            
            print(f"{status} {url} - {code} ({time_ms:.0f}ms)")
            if result['error']:
                print(f"  Error: {result['error']}")
        
        if args.output:
            output_path = Path(args.output)
            if output_path.suffix == '.json':
                monitor.export_json(output_path)
            elif output_path.suffix == '.csv':
                monitor.export_csv(output_path)
            print(f"\n✓ Exported to {args.output}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
