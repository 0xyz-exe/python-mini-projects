# Duplicate File Finder

Find duplicate files by cryptographic hash.

## Features

- MD5 hash comparison
- Streaming for large files
- Minimum size filter
- Wasted space calculation
- Report-only (no deletion)

## Usage

```bash
cd projects/10-duplicate-file-finder/src

# Find duplicates
python cli.py ~/Documents

# Filter by minimum size (1KB)
python cli.py ~/Documents --min-size 1024
```

## Testing

```bash
cd projects/10-duplicate-file-finder
python tests/test_duplicate_finder.py
```

## Dependencies

Python 3.11+ (stdlib only)

## Safety

- Report only, no automatic deletion
- Streaming hash for large files
- User must manually review results
