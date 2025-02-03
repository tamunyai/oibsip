import random
import string


class InvalidPasswordLengthError(Exception):
    """Exception raised for invalid password length."""

    pass


class NoCharacterTypesSelectedError(Exception):
    """Exception raised when no character types are selected for the password."""

    pass


def get_user_preference(prompt: str) -> bool:
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()

        if choice in ["y", "n"]:
            return choice == "y"

        print("Invalid input. Please enter 'y' or 'n'.")


def generate_password(
    length: int,
    use_uppercase: bool,
    use_lowercase: bool,
    use_digits: bool,
    use_symbols: bool,
    minimum_numbers: int = 1,
    minimum_special: int = 1,
) -> str:
    if length < 5:
        raise InvalidPasswordLengthError("Password length must be at least 5.")

    character_pool = ""
    password_chars = []

    if use_uppercase:
        character_pool += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))

    if use_lowercase:
        character_pool += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))

    if use_digits:
        character_pool += string.digits
        digits = random.choices(string.digits, k=minimum_numbers)
        password_chars.extend("".join(digits))

    if use_symbols:
        character_pool += string.punctuation
        sympols = random.choices(string.punctuation, k=minimum_special)
        password_chars.extend("".join(sympols))

    if not character_pool:
        raise NoCharacterTypesSelectedError(
            "No character types selected. Please select at least one."
        )

    for _ in range(length - len(password_chars)):
        password_chars.extend(random.choice(character_pool))

    random.shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("Random Password Generator")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 5:
                raise InvalidPasswordLengthError("Password length must be at least 5.")

            break

        except ValueError:
            print("Error: Please enter a valid number for password length.")

        except InvalidPasswordLengthError as e:
            print(f"Error: {e}")

    use_uppercase = get_user_preference("Include uppercase letters?")
    use_lowercase = get_user_preference("Include lowercase letters?")
    use_digits = get_user_preference("Include numbers?")
    use_symbols = get_user_preference("Include special characters?")

    try:
        password = generate_password(
            length, use_uppercase, use_lowercase, use_digits, use_symbols
        )
        print(f"Generated Password: {password}")

    except InvalidPasswordLengthError as e:
        print(f"Error: {e}")

    except NoCharacterTypesSelectedError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
