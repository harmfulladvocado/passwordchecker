# Password Strength Checker

A Python tool that evaluates password strength using entropy analysis and pattern detection.

## Features

- **Shannon Entropy Calculation**: Measures password randomness in bits
- **Character Class Detection**: Checks for lowercase, uppercase, digits, symbols, and special characters
- **Pattern Detection**:
  - Common passwords (e.g., "password", "123456")
  - Sequential patterns (e.g., "abcd", "1234")
  - Keyboard row patterns (e.g., "qwerty", "asdf")
  - Repeated characters (e.g., "aaaa", "1111")
- **Strength Rating**: Categorizes passwords as Poor, Weak, Good, or Very Good
- **Actionable Suggestions**: Provides specific recommendations to improve password security

## Usage

Run the script:

```bash
python "password checker.py"
```

Enter a password when prompted to receive an analysis including:
- Password length
- Entropy (in bits)
- Strength rating
- Character classes used
- Security suggestions

## Strength Criteria

| Entropy (bits) | Strength Rating |
|----------------|-----------------|
| < 28           | Poor            |
| 28 - 35        | Weak            |
| 36 - 59        | Good            |
| ≥ 60           | Very Good       |

## Example Output

```
Entered password: MyP@ssw0rd
Result:
Length: 10
Entropy (bits): 42.5
Strength: Good
Detected character classes: lower, upper, digit, symbol

Suggestions:
- Consider a password of 12+ characters for better security.
```

## Requirements

- Python 3.x
- Standard library only (no external dependencies)
