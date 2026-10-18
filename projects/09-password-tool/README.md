# Password Generator and Security Checker

Local password generation and basic strength checking.

## Features

- Generate passwords using `secrets` module
- Configurable length and character sets
- Basic strength analysis
- No external APIs (fully offline)
- No password logging

## Usage

```bash
cd projects/09-password-tool/src

# Generate password
python cli.py generate

# Custom length
python cli.py generate -l 24

# No symbols
python cli.py generate --no-symbols

# Check password strength
python cli.py check "MyPassword123!"
```

## Testing

```bash
cd projects/09-password-tool
python tests/test_password_tool.py
```

## Dependencies

Python 3.11+ (stdlib only)

## Limitations

- No breach database check
- No entropy calculation
- Basic heuristics only
- Never send passwords to external services
