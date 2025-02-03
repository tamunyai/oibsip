import string
from unittest.mock import patch

import pytest
from random_password_generator import (
    InvalidPasswordLengthError,
    NoCharacterTypesSelectedError,
    generate_password,
    get_user_preference
)


@patch("builtins.input", side_effect=["invalid", "y"])
def test_get_user_preference(mock_input):
    result = get_user_preference("Do you want uppercase?")
    assert result == True


def test_generate_password_with_all_options():
    password = generate_password(
        length=12,
        use_uppercase=True,
        use_lowercase=True,
        use_digits=True,
        use_symbols=True,
        minimum_numbers=2,
        minimum_special=2,
    )

    assert len(password) == 12
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)


def test_generate_password_with_missing_options():
    password = generate_password(
        length=10,
        use_uppercase=False,
        use_lowercase=True,
        use_digits=True,
        use_symbols=False,
        minimum_numbers=2,
        minimum_special=0,
    )

    assert len(password) == 10
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert not any(c in string.punctuation for c in password)
    assert not any(c in string.ascii_uppercase for c in password)


def test_generate_password_no_character_types():
    with pytest.raises(NoCharacterTypesSelectedError):
        generate_password(
            length=10,
            use_uppercase=False,
            use_lowercase=False,
            use_digits=False,
            use_symbols=False,
        )


def test_generate_password_invalid_length():
    with pytest.raises(InvalidPasswordLengthError):
        generate_password(
            length=-5,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_symbols=True,
        )


def test_generate_password_minimum_requirements():
    password = generate_password(
        length=8,
        use_uppercase=True,
        use_lowercase=True,
        use_digits=True,
        use_symbols=True,
        minimum_numbers=3,
        minimum_special=2,
    )

    assert sum(c in string.digits for c in password) >= 3
    assert sum(c in string.punctuation for c in password) >= 2


if __name__ == "__main__":
    pytest.main()
