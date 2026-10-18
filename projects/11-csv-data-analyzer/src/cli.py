#!/usr/bin/env python3
"""CSV Analyzer CLI."""
import argparse
from pathlib import Path
from csv_analyzer import CSVAnalyzer


def main():
    parser = argparse.ArgumentParser(description="CSV analyzer")
    parser.add_argument("csv_file")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("summary")
    subparsers.add_parser("missing")
    
    stats = subparsers.add_parser("stats")
    stats.add_argument("column")
    
    group = subparsers.add_parser("group")
    group.add_argument("column")
    
    clean = subparsers.add_parser("clean")
    clean.add_argument("output")
    
    args = parser.parse_args()
    
    try:
        analyzer = CSVAnalyzer(Path(args.csv_file))
        analyzer.load()
        
        if args.command == "summary":
            summary = analyzer.summary()
            for k, v in summary.items():
                print(f"{k}: {v}")
        
        elif args.command == "missing":
            missing = analyzer.missing_values()
            if missing:
                for col, count in missing.items():
                    print(f"{col}: {count} missing")
            else:
                print("No missing values")
        
        elif args.command == "stats":
            stats = analyzer.numeric_stats(args.column)
            for k, v in stats.items():
                print(f"{k}: {v}")
        
        elif args.command == "group":
            groups = analyzer.group_by(args.column)
            for key, count in groups.items():
                print(f"{key}: {count}")
        
        elif args.command == "clean":
            analyzer.export_cleaned(Path(args.output), drop_empty_rows=True)
            print(f"✓ Exported to {args.output}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
