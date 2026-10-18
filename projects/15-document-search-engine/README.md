# Local Document Search Engine

Index and search local text documents.

## Features

- Index .txt and .md files
- Tokenization and normalization
- Inverted index for fast search
- Relevance scoring
- JSON persistence
- Search result snippets

## Usage

```bash
cd projects/15-document-search-engine/src

# Index directory
python cli.py index ~/Documents

# Index specific extensions
python cli.py index ~/Documents -e .txt .md .py

# Search
python cli.py search "python programming"

# Limit results
python cli.py search "python" -n 5
```

## Testing

```bash
cd projects/15-document-search-engine
python tests/test_search_engine.py
```

## Dependencies

Python 3.11+ (stdlib only)

## Limitations

- No stemming or lemmatization
- Simple token matching
- No phrase search
- No ranking by TF-IDF
- Local files only
