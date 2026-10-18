#!/usr/bin/env python3
"""File Organizer - CLI."""
import argparse
from pathlib import Path
from file_organizer import FileOrganizer


def main():
    parser = argparse.ArgumentParser(description="Organize files")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("destination", help="Destination directory")
    parser.add_argument("-m", "--mode", choices=["extension", "type"], 
                       default="extension", help="Organization mode")
    parser.add_argument("--dry-run", action="store_true", 
                       help="Preview without moving files")
    
    args = parser.parse_args()
    
    try:
        organizer = FileOrganizer(Path(args.source), Path(args.destination))
        
        if args.mode == "extension":
            result = organizer.organize_by_extension(dry_run=args.dry_run)
        else:
            result = organizer.organize_by_type(dry_run=args.dry_run)
        
        print(f"{'DRY RUN - ' if args.dry_run else ''}Organization Summary:")
        for category, files in result.items():
            print(f"{category}: {len(files)} files")
        
        if not args.dry_run:
            print(f"\n✓ Organized {sum(len(f) for f in result.values())} files")
            if organizer.get_log():
                print("\nLog saved. First 5 operations:")
                for entry in organizer.get_log()[:5]:
                    print(f"  {entry}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
