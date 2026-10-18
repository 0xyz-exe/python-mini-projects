# Python Mini Projects

Collection of 15 functional, tested Python projects for learning and portfolio.

## Projects

### 01. CLI Task Manager
Command-line task manager with priorities, deadlines, and filters. JSON persistence.

**Features:** Add/edit/delete tasks, priorities, status filters  
**Tech:** Python stdlib, argparse, JSON  
**Path:** `projects/01-cli-task-manager/`

### 02. Expense Tracker
Personal finance tracker with categories and monthly summaries.

**Features:** Income/expense tracking, CSV import/export, monthly reports  
**Tech:** Python stdlib, CSV  
**Path:** `projects/02-expense-tracker/`

### 03. File Organizer
Organize files by extension or type with dry-run preview.

**Features:** Extension/type organization, collision handling, safe copy  
**Tech:** Python stdlib, pathlib  
**Path:** `projects/03-file-organizer/`

### 04. Batch File Renamer
Batch rename files with preview and collision detection.

**Features:** Prefix/suffix, numbering, find-replace, dry-run  
**Tech:** Python stdlib  
**Path:** `projects/04-batch-file-renamer/`

### 05. Text and Log Analyzer
Analyze text files and application logs.

**Features:** Word count, frequent terms, log levels, filtering  
**Tech:** Python stdlib, regex  
**Path:** `projects/05-text-log-analyzer/`

### 06. FastAPI REST API
Task/notes REST API with CRUD operations.

**Features:** CRUD endpoints, Pydantic validation, OpenAPI docs  
**Tech:** FastAPI, uvicorn  
**Path:** `projects/06-fastapi-rest-api/`

### 07. Web Scraper
Responsible web scraping with BeautifulSoup.

**Features:** Extract titles/headings/links, JSON/CSV export  
**Tech:** requests, BeautifulSoup4  
**Path:** `projects/07-web-scraper/`

### 08. Weather CLI
Weather app using Open-Meteo API (free, no key required).

**Features:** Current weather, offline demo mode  
**Tech:** requests, Open-Meteo API  
**Path:** `projects/08-weather-cli/`

### 09. Password Generator and Security Checker
Local password generation and strength checking.

**Features:** Secure generation via secrets module, strength analysis  
**Tech:** Python stdlib (secrets)  
**Path:** `projects/09-password-tool/`

### 10. Duplicate File Finder
Find duplicate files by cryptographic hash.

**Features:** MD5 hash, streaming for large files, wasted space calc  
**Tech:** Python stdlib (hashlib)  
**Path:** `projects/10-duplicate-file-finder/`

### 11. CSV Data Analyzer
Analyze and clean CSV data.

**Features:** Stats, missing values, grouping, numeric analysis  
**Tech:** Python stdlib (csv)  
**Path:** `projects/11-csv-data-analyzer/`

### 12. Machine Learning Classifier
ML classifier using scikit-learn and iris dataset.

**Features:** Train RandomForest, metrics, model persistence  
**Tech:** scikit-learn  
**Path:** `projects/12-ml-classifier/`

### 13. AI Chatbot
Chatbot with deterministic rule-based mode (offline).

**Features:** Rule-based responses, conversation history  
**Tech:** Python stdlib  
**Path:** `projects/13-ai-chatbot/`

### 14. Website Availability Monitor
Monitor website health and response times.

**Features:** HTTP status, response time, JSON/CSV export  
**Tech:** requests  
**Path:** `projects/14-website-monitor/`

### 15. Local Document Search Engine
Index and search local text documents.

**Features:** Inverted index, relevance scoring, persistence  
**Tech:** Python stdlib (regex, json)  
**Path:** `projects/15-document-search-engine/`

## Quick Start

### Prerequisites
- Python 3.11+ (Python 3.13.14 tested)
- Git
- pip

### Installation

```bash
# Clone repository
cd python-mini-projects

# Projects 1-5, 9-11, 13, 15: stdlib only
cd projects/01-cli-task-manager
python tests/test_task_manager.py

# Projects with optional dependencies:
# Project 06 (FastAPI)
python3 -m pip install fastapi uvicorn --user

# Project 07 (Web Scraper)
python3 -m pip install requests beautifulsoup4 --user

# Project 08 (Weather)
python3 -m pip install requests --user

# Project 12 (ML)
python3 -m pip install scikit-learn --user

# Project 14 (Monitor)
python3 -m pip install requests --user
```

### Run Tests

```bash
# Test all stdlib projects
python3 projects/01-cli-task-manager/tests/test_task_manager.py
python3 projects/02-expense-tracker/tests/test_expense_tracker.py
python3 projects/03-file-organizer/tests/test_file_organizer.py
python3 projects/04-batch-file-renamer/tests/test_file_renamer.py
python3 projects/05-text-log-analyzer/tests/test_text_analyzer.py
python3 projects/09-password-tool/tests/test_password_tool.py
python3 projects/10-duplicate-file-finder/tests/test_duplicate_finder.py
python3 projects/11-csv-data-analyzer/tests/test_csv_analyzer.py
python3 projects/13-ai-chatbot/tests/test_chatbot.py
python3 projects/15-document-search-engine/tests/test_search_engine.py

# Projects with dependencies (install first)
python3 projects/06-fastapi-rest-api/tests/test_api.py
python3 projects/07-web-scraper/tests/test_scraper.py
python3 projects/08-weather-cli/tests/test_weather.py
python3 projects/12-ml-classifier/tests/test_ml_classifier.py
python3 projects/14-website-monitor/tests/test_monitor.py
```

## Project Structure

```
python-mini-projects/
├── README.md                  # This file
├── LICENSE                    # MIT License
├── .gitignore
└── projects/
    ├── 01-cli-task-manager/
    │   ├── README.md
    │   ├── src/
    │   │   ├── task_manager.py
    │   │   └── cli.py
    │   └── tests/
    │       └── test_task_manager.py
    ├── 02-expense-tracker/
    ├── ...
    └── 15-document-search-engine/
```

## Engineering Standards

- **Type hints** where practical
- **Error handling** with meaningful messages
- **Input validation** at boundaries
- **Tests** for core functionality
- **Documentation** in README per project
- **No hardcoded secrets** or credentials
- **Modular code** with focused functions

## Security Notes

- No API keys committed to repo
- Passwords never logged
- User input validated
- Safe file operations (no automatic deletion)
- External requests use timeouts
- Pickle only for user's own trained models

## Dependencies

### Stdlib Only (10 projects)
Projects 01-05, 09-11, 13, 15

### Optional Dependencies (5 projects)
- **FastAPI + uvicorn:** Project 06
- **requests + BeautifulSoup4:** Project 07
- **requests:** Projects 08, 14
- **scikit-learn:** Project 12

## Testing

All projects include tests. Projects with optional dependencies gracefully skip tests when dependencies unavailable.

## Windows Compatibility

Tested on Windows 11 with Python 3.13.14. Uses:
- Forward-slash paths for cross-platform
- `pathlib` for filesystem operations
- Git Bash for terminal commands

## License

MIT License - See LICENSE file

## Contributing

These are educational projects. Feel free to:
- Add features
- Improve tests
- Fix bugs
- Enhance documentation

## Known Limitations

- **Project 12 (ML):** Toy dataset, no hyperparameter tuning
- **Project 07 (Scraper):** Basic extraction only
- **Project 13 (Chatbot):** Simple rule-based, no NLP
- **Project 15 (Search):** No TF-IDF or stemming

## Future Enhancements

- CI/CD with GitHub Actions
- Additional test coverage
- Performance benchmarks
- Docker containers
- API documentation
- More projects

## Author

Built with Hermes Agent on 2026-10-18

## Acknowledgments

- Python Software Foundation
- Open-source library maintainers
- Educational content inspiration
