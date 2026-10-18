"""AI Chatbot with local fallback."""
import os
from typing import List, Dict


class Chatbot:
    """Simple chatbot with rule-based fallback."""
    
    def __init__(self, mode: str = "rule"):
        self.mode = mode
        self.history: List[Dict[str, str]] = []
        self.rules = {
            "hello": "Hi there! How can I help you?",
            "hi": "Hello! What can I do for you?",
            "how are you": "I'm doing well, thanks for asking!",
            "bye": "Goodbye! Have a great day!",
            "help": "I can chat with you. Try saying hello!",
        }
    
    def chat(self, message: str) -> str:
        """Process message and return response."""
        self.history.append({"role": "user", "content": message})
        
        if self.mode == "rule":
            response = self._rule_based_response(message)
        else:
            response = "AI mode not configured (use --mode rule for local)"
        
        self.history.append({"role": "assistant", "content": response})
        return response
    
    def _rule_based_response(self, message: str) -> str:
        """Deterministic rule-based responses."""
        message_lower = message.lower().strip()
        
        for pattern, response in self.rules.items():
            if pattern in message_lower:
                return response
        
        return "I'm a simple chatbot. Try: hello, help, or bye."
    
    def reset(self):
        """Clear conversation history."""
        self.history.clear()
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get conversation history."""
        return self.history.copy()
