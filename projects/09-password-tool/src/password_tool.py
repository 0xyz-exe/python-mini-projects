"""Password Generator and Security Checker."""
import secrets
import string
from typing import Dict


class PasswordTool:
    """Generate and check passwords locally."""
    
    def generate(self, length: int = 16, use_upper: bool = True, 
                 use_lower: bool = True, use_digits: bool = True, 
                 use_symbols: bool = True) -> str:
        """Generate secure password using secrets module."""
        if length < 4:
            raise ValueError("Password length must be at least 4")
        
        charset = ""
        if use_lower:
            charset += string.ascii_lowercase
        if use_upper:
            charset += string.ascii_uppercase
        if use_digits:
            charset += string.digits
        if use_symbols:
            charset += "!@#$%^&*()-_=+[]{}|;:,.<>?"
        
        if not charset:
            raise ValueError("At least one character set must be enabled")
        
        return ''.join(secrets.choice(charset) for _ in range(length))
    
    def check_strength(self, password: str) -> Dict:
        """Basic password strength check."""
        # ponytail: no breach DB check, no entropy calc
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password)
        
        score = 0
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if length >= 16:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_symbol:
            score += 1
        
        strength = "weak"
        if score >= 5:
            strength = "medium"
        if score >= 7:
            strength = "strong"
        
        return {
            'length': length,
            'has_upper': has_upper,
            'has_lower': has_lower,
            'has_digit': has_digit,
            'has_symbol': has_symbol,
            'score': score,
            'strength': strength
        }
