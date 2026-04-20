# L28-Homework---NonLLM-Tool
# Password Entropy Tool

## Tool Name and Purpose
The password entropy tool tests the strength of an inputted password. This tool uses the formula $L \times \log_2(R)$ to calculate the bit count of the password's resistance to brute force attacks.

## Installation
pip install pytest

## Usage Example
from tool import calculate_password_entropy

analysis = calculate_password_entropy("Secure!2026")
print(analysis)
# Output: {'result': 72.05, 'unit': 'bits', 'detail': 'This password has a strength rating of: Moderate'}