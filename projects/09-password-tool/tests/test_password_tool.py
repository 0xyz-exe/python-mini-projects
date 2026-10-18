"""Tests for password tool."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from password_tool import PasswordTool


def test_generate_password():
    tool = PasswordTool()
    pwd = tool.generate(length=16)
    assert len(pwd) == 16


def test_generate_custom():
    tool = PasswordTool()
    pwd = tool.generate(length=20, use_symbols=False)
    assert len(pwd) == 20
    assert not any(c in "!@#$" for c in pwd)


def test_check_weak():
    tool = PasswordTool()
    result = tool.check_strength("abc123")
    assert result['strength'] == "weak"


def test_check_strong():
    tool = PasswordTool()
    result = tool.check_strength("Abc123!@#XyzLongPassword")
    assert result['strength'] == "strong"
    assert result['has_upper']
    assert result['has_lower']
    assert result['has_digit']
    assert result['has_symbol']


def test_invalid_length():
    tool = PasswordTool()
    try:
        tool.generate(length=2)
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_generate_password()
    test_generate_custom()
    test_check_weak()
    test_check_strong()
    test_invalid_length()
    print("✓ All tests passed")
