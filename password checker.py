import string
import math
import collections

COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "qwerty", "abc123",
    "111111", "1234567", "iloveyou", "admin", "welcome", "letmein",
}

KEYBOARD_ROWS = ["`1234567890-=", "qwertyuiop[]\\", "asdfghjkl;'", "zxcvbnm,./"]


def shannon_entropy(password: str) -> float:
    if not password:
        return 0.0
    counts = collections.Counter(password)
    length = len(password)
    entropy_per_char = 0.0
    for cnt in counts.values():
        p = cnt / length
        entropy_per_char -= p * math.log2(p)
    return entropy_per_char * length


def has_long_sequence(pw: str, seq_len: int = 4) -> bool:
    s = pw.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    sequences = [alpha, alpha[::-1], digits, digits[::-1]]
    sequences += KEYBOARD_ROWS + [r[::-1] for r in KEYBOARD_ROWS]
    for L in range(seq_len, len(s) + 1):
        for i in range(len(s) - L + 1):
            sub = s[i:i + L]
            for seq in sequences:
                if sub in seq:
                    return True
    return False


def max_repetition_run(pw: str) -> int:
    if not pw:
        return 0
    max_run = cur = 1
    for a, b in zip(pw, pw[1:]):
        if a == b:
            cur += 1
            if cur > max_run:
                max_run = cur
        else:
            cur = 1
    return max_run


def character_classes(password: str) -> dict:
    return {
        "lower": any(c.islower() for c in password),
        "upper": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "symbol": any(c in string.punctuation for c in password),
        "other": any(not (c.isalnum() or c in string.punctuation) for c in password),
    }


def evaluate(password: str) -> dict:
    ent = shannon_entropy(password)
    classes = character_classes(password)
    length = len(password)
    suggestions = []

    if ent < 28:
        strength = "Poor"
    elif ent < 36:
        strength = "Weak"
    elif ent < 60:
        strength = "Good"
    else:
        strength = "Very good"

    if length < 8:
        suggestions.append("Increase the password length to at least 12 characters.")
    elif length < 12:
        suggestions.append("Consider a password of 12+ characters for better security.")

    if not classes["upper"]:
        suggestions.append("Add uppercase letters.")
    if not classes["lower"]:
        suggestions.append("Add lowercase letters.")
    if not classes["digit"]:
        suggestions.append("Add digits.")
    if not classes["symbol"]:
        suggestions.append("Add punctuation/symbols (e.g. !@#$%).")

    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Do not use a common password.")
    if has_long_sequence(password, seq_len=4):
        suggestions.append("Avoid obvious sequences like 'abcd', '1234' or keyboard row patterns.")
    if max_repetition_run(password) >= max(3, length // 2):
        suggestions.append("Avoid repeated characters (e.g. 'aaaaaa' or '111111').")

    if not suggestions:
        suggestions.append("Good password. Consider a password manager for unique passwords per service.")

    return {
        "password": password,
        "length": length,
        "entropy_bits": round(ent, 2),
        "classes": classes,
        "strength": strength,
        "suggestions": suggestions,
    }


def main():
    pw = input("Enter the password you want to check (input will be shown):\n")

    result = evaluate(pw)

    print("\nEntered password:", pw)
    print("Result:")
    print("Length:", result["length"])
    print("Entropy (bits):", result["entropy_bits"])
    print("Strength:", result["strength"])
    print("Detected character classes:", ", ".join([k for k, v in result["classes"].items() if v]))
    print("\nSuggestions:")
    for s in result["suggestions"]:
        print("-", s)


if __name__ == "__main__":
    main()
