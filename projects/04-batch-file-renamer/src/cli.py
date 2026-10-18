#!/usr/bin/env python3
"""Batch File Renamer - CLI."""
import argparse
from pathlib import Path
from file_renamer import FileRenamer


def main():
    parser = argparse.ArgumentParser(description="Batch rename files")
    parser.add_argument("directory", help="Directory containing files")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("-e", "--extensions", nargs="+", help="Filter by extensions")
    
    subparsers = parser.add_subparsers(dest="mode", required=True)
    
    prefix = subparsers.add_parser("prefix", help="Add prefix")
    prefix.add_argument("text", help="Prefix text")
    
    suffix = subparsers.add_parser("suffix", help="Add suffix")
    suffix.add_argument("text", help="Suffix text")
    
    number = subparsers.add_parser("number", help="Add sequential numbers")
    number.add_argument("-s", "--start", type=int, default=1, help="Start number")
    
    replace = subparsers.add_parser("replace", help="Find and replace")
    replace.add_argument("find", help="Text to find")
    replace.add_argument("replace", help="Replacement text")
    
    args = parser.parse_args()
    
    try:
        renamer = FileRenamer(Path(args.directory))
        
        if args.mode == "prefix":
            operations = renamer.add_prefix(args.text, args.extensions)
        elif args.mode == "suffix":
            operations = renamer.add_suffix(args.text, args.extensions)
        elif args.mode == "number":
            operations = renamer.add_numbering(args.start, args.extensions)
        elif args.mode == "replace":
            operations = renamer.find_replace(args.find, args.replace, args.extensions)
        
        if not operations:
            print("No files to rename")
            return 0
        
        print(f"{'[DRY RUN] ' if args.dry_run else ''}Preview:")
        for old_path, new_path in operations:
            print(f"  {old_path.name} -> {new_path.name}")
        
        if not args.dry_run:
            log = renamer.execute(dry_run=False)
            print(f"\n✓ Renamed {len(log)} files")
        else:
            print(f"\n{len(operations)} files would be renamed")
            print("Run without --dry-run to execute")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
