# Batch File Renamer

Batch rename files with preview and collision detection.

## Features

- Add prefix/suffix
- Sequential numbering
- Find and replace
- Extension filtering
- Collision detection
- Dry-run preview

## Usage

```bash
cd projects/04-batch-file-renamer/src

# Preview with prefix
python cli.py ~/Documents prefix "2026_" --dry-run

# Add suffix to txt files
python cli.py ~/Documents suffix "_backup" -e txt

# Sequential numbering starting at 100
python cli.py ~/Photos number -s 100

# Find and replace
python cli.py ~/Files replace "old_name" "new_name"
```

## Testing

```bash
cd projects/04-batch-file-renamer
python tests/test_file_renamer.py
```

## Dependencies

Python 3.11+ (stdlib only)

## Safety

- Dry-run preview required by default
- Collision detection prevents overwrites
- Extension filtering for precision
