# tool.py
# ---------------------------------------------------------
# Tool Name : calculate_password_entropy
# Domain    : Cybersecurity
# Author    : Jalon Rivers
# Description: Computes the information entropy of a password string 
#              to measure its unpredictable strength in bits.
# Usage     : See README.md for a sample call.
# ---------------------------------------------------------

import math

def calculate_password_entropy(password: str) -> dict:
    """
    Calculates the Shannon entropy of a password based on character pool size.

    Args:
        password (str): The raw password string to evaluate.

    Returns:
        dict: {
            "result": float,
            "unit": "bits",
            "detail": str
        }

    Raises:
        ValueError: If the password is empty or not a string.
    """
    if not isinstance(password, str):
        raise ValueError("Input must be a string.")
    
    if len(password) == 0:
        raise ValueError("Password cannot be empty.")

    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(not c.isalnum() for c in password): pool_size += 32

    entropy = len(password) * math.log2(pool_size)
    entropy = round(entropy, 2)

    strength = "Very Weak"
    if entropy >= 80: strength = "Strong"
    elif entropy >= 60: strength = "Moderate"
    elif entropy >= 36: strength = "Weak"

    return {
        "result": entropy,
        "unit": "bits",
        "detail": f"This password has a strength rating of: {strength}"
    }