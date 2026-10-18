#!/usr/bin/env python3
"""Duplicate File Finder CLI."""
import argparse
from pathlib import Path
from duplicate_finder import DuplicateFinder


def main():
    parser = argparse.ArgumentParser(description="Find duplicate files")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("--min-size", type=int, default=0, help="Minimum file size")
    
    args = parser.parse_args()
    
    try:
        finder = DuplicateFinder(Path(args.directory))
        print(f"Scanning {args.directory}...")
        
        duplicates = finder.find_duplicates(min_size=args.min_size)
        
        if not duplicates:
            print("No duplicates found")
            return 0
        
        for file_hash, files in duplicates.items():
            print(f"\nDuplicate group ({file_hash[:8]}):")
            for file_path in files:
                print(f"  {file_path}")
        
        summary = finder.get_summary()
        print(f"\n{'='*50}")
        print(f"Groups: {summary['duplicate_groups']}")
        print(f"Files: {summary['total_duplicate_files']}")
        print(f"Wasted: {summary['wasted_space_bytes']:,} bytes")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
