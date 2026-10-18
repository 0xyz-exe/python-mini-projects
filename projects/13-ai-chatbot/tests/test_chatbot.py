"""Tests for chatbot."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from chatbot import Chatbot


def test_rule_based():
    bot = Chatbot(mode="rule")
    response = bot.chat("hello")
    assert "Hi" in response or "Hello" in response


def test_history():
    bot = Chatbot(mode="rule")
    bot.chat("hi")
    bot.chat("bye")
    
    history = bot.get_history()
    assert len(history) == 4  # 2 user + 2 assistant


def test_reset():
    bot = Chatbot(mode="rule")
    bot.chat("hello")
    bot.reset()
    
    history = bot.get_history()
    assert len(history) == 0


def test_unknown_input():
    bot = Chatbot(mode="rule")
    response = bot.chat("random gibberish xyz")
    assert "simple chatbot" in response.lower()


if __name__ == "__main__":
    test_rule_based()
    test_history()
    test_reset()
    test_unknown_input()
    print("✓ All tests passed")
