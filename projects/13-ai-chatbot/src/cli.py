#!/usr/bin/env python3
"""AI Chatbot CLI."""
from chatbot import Chatbot


def main():
    print("Chatbot (type 'exit' to quit, 'reset' to clear history)")
    print("Mode: rule-based (deterministic, offline)\n")
    
    bot = Chatbot(mode="rule")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            if user_input.lower() == "reset":
                bot.reset()
                print("History cleared.\n")
                continue
            
            response = bot.chat(user_input)
            print(f"Bot: {response}\n")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            break
    
    return 0


if __name__ == "__main__":
    exit(main())
