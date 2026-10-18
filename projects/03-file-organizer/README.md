# File Organizer

Organize files by extension or type with dry-run preview.

## Features

- Organize by extension
- Organize by type (images, documents, videos, etc.)
- Dry-run mode
- Collision handling (automatic renaming)
- Operation logging
- Safe copy operation

## Usage

```bash
cd projects/03-file-organizer/src

# Dry run (preview)
python cli.py ~/Downloads ~/Organized --dry-run

# Organize by extension
python cli.py ~/Downloads ~/Organized -m extension

# Organize by type
python cli.py ~/Downloads ~/Organized -m type
```

## Testing

```bash
cd projects/03-file-organizer
python tests/test_file_organizer.py
```

## Dependencies

Python 3.11+ (stdlib only)

## Safety

- Uses copy, not move (originals preserved)
- Collision detection and auto-rename
- Dry-run preview before execution
