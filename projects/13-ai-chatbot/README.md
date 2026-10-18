# AI Chatbot with Local Fallback

Modular chatbot with deterministic rule-based mode.

## Features

- Rule-based mode (offline, deterministic)
- Conversation history
- Reset command
- No API required for default mode
- Extensible architecture

## Usage

```bash
cd projects/13-ai-chatbot/src

# Run chatbot
python cli.py

# Chat commands:
# - Type messages normally
# - 'reset' to clear history
# - 'exit' to quit
```

## Testing

```bash
cd projects/13-ai-chatbot
python tests/test_chatbot.py
```

## Dependencies

Python 3.11+ (stdlib only for rule mode)

## Extension

To add AI provider:
1. Add provider adapter in chatbot.py
2. Handle API calls with timeouts
3. Use environment variables for credentials
4. Keep rule mode as default

## Limitations

- Rule mode has limited vocabulary
- No sentiment analysis
- No context understanding
- Educational demo only
