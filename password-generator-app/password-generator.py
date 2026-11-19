import secrets
import string


def generate_password(seed_text: str) -> str:
    if not isinstance(seed_text, str):
        raise TypeError("Input must be a string.")

    categories = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]
    all_chars = "".join(categories)

    if len(seed_text) < len(categories):
        raise ValueError(f"Input must be at least {len(categories)} characters long.")

    # Ensure every character in the input belongs to the allowed categories
    if any(ch not in all_chars for ch in seed_text):
        raise ValueError("Input contains invalid characters (spaces or unsupported symbols).")

    # Ensure the input includes at least one character from each category
    if not all(any(ch in cat for ch in seed_text) for cat in categories):
        raise ValueError(
            "Input must include at least one uppercase letter, lowercase letter, digit, and punctuation mark."
        )

    # Generate a cryptographically secure password of the exact same length
    length = len(seed_text)
    password_chars = [secrets.choice(cat) for cat in categories]
    password_chars += [secrets.choice(all_chars) for _ in range(length - len(categories))]

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    while True:
        user_str = input("Enter a valid string (min 4 chars, with upper, lower, digit, and symbol): ")
        try:
            print(generate_password(user_str))
            break
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
