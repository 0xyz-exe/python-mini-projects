#!/usr/bin/env python3
"""Password Tool CLI."""
import argparse
from password_tool import PasswordTool


def main():
    parser = argparse.ArgumentParser(description="Password tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    gen = subparsers.add_parser("generate", help="Generate password")
    gen.add_argument("-l", "--length", type=int, default=16)
    gen.add_argument("--no-upper", action="store_true")
    gen.add_argument("--no-lower", action="store_true")
    gen.add_argument("--no-digits", action="store_true")
    gen.add_argument("--no-symbols", action="store_true")
    
    check = subparsers.add_parser("check", help="Check password strength")
    check.add_argument("password")
    
    args = parser.parse_args()
    tool = PasswordTool()
    
    try:
        if args.command == "generate":
            password = tool.generate(
                length=args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols
            )
            print(password)
        
        elif args.command == "check":
            result = tool.check_strength(args.password)
            print(f"Length: {result['length']}")
            print(f"Uppercase: {'✓' if result['has_upper'] else '✗'}")
            print(f"Lowercase: {'✓' if result['has_lower'] else '✗'}")
            print(f"Digits: {'✓' if result['has_digit'] else '✗'}")
            print(f"Symbols: {'✓' if result['has_symbol'] else '✗'}")
            print(f"Strength: {result['strength']} (score: {result['score']}/7)")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
