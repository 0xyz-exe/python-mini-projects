#!/usr/bin/env python3
"""Text and Log Analyzer - CLI."""
import argparse
from pathlib import Path
from text_analyzer import TextAnalyzer


def main():
    parser = argparse.ArgumentParser(description="Analyze text and log files")
    parser.add_argument("file", help="File to analyze")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    subparsers.add_parser("stats", help="Basic statistics")
    
    freq = subparsers.add_parser("frequent", help="Frequent words")
    freq.add_argument("-n", "--top", type=int, default=10)
    
    subparsers.add_parser("logs", help="Log severity analysis")
    
    filter_cmd = subparsers.add_parser("filter", help="Filter log entries")
    filter_cmd.add_argument("-k", "--keyword")
    filter_cmd.add_argument("-d", "--date")
    
    export = subparsers.add_parser("export", help="Export report")
    export.add_argument("output")
    export.add_argument("-f", "--format", choices=["json", "csv"], default="json")
    
    args = parser.parse_args()
    
    try:
        analyzer = TextAnalyzer(Path(args.file))
        
        if args.command == "stats":
            stats = analyzer.count_stats()
            for key, val in stats.items():
                print(f"{key}: {val}")
        
        elif args.command == "frequent":
            freq = analyzer.frequent_words(args.top)
            for word, count in freq:
                print(f"{word}: {count}")
        
        elif args.command == "logs":
            levels = analyzer.analyze_logs()
            for level, count in levels.items():
                print(f"{level}: {count}")
        
        elif args.command == "filter":
            results = analyzer.filter_logs(args.keyword, args.date)
            for line in results:
                print(line)
        
        elif args.command == "export":
            analyzer.export_report(Path(args.output), args.format)
            print(f"✓ Exported to {args.output}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
