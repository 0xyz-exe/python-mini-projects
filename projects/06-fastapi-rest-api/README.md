# FastAPI REST API

Task/notes REST API with CRUD operations.

## Features

- CRUD endpoints
- Pydantic validation
- JSON persistence
- OpenAPI documentation
- HTTP status codes
- Error responses

## Setup

```bash
cd projects/06-fastapi-rest-api
python3 -m pip install fastapi uvicorn --user
```

## Usage

```bash
cd projects/06-fastapi-rest-api/src

# Run server
python main.py

# API available at http://127.0.0.1:8000
# Docs at http://127.0.0.1:8000/docs
```

## API Endpoints

- `GET /notes` - List all notes
- `GET /notes/{id}` - Get note by ID
- `POST /notes` - Create note
- `PUT /notes/{id}` - Update note
- `DELETE /notes/{id}` - Delete note

## Testing

```bash
cd projects/06-fastapi-rest-api
python tests/test_api.py
```

## Dependencies

- Python 3.11+
- fastapi
- uvicorn
