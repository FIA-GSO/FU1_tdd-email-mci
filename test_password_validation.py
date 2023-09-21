import pytest
from password_validation import is_valid_password

# Liste von validen Passwörtern
valid_passwords = [
    # Mindestens 8 Zeichen und 4 Arten von Zeichen (bei mindestens 25 Zeichen müssen nur 2 Arten von Zeichen vorkommen)
    "H$llo123",  # 8 Zeichen, 4 Arten
    'H$llo123H$llo123H$llo123',  # 24 Zeichen, 4 Arten
    'abcdefghijklmnopqrstuvw12',  # 25 Zeichen, 2 Arten
    'H$llo12345678901234567890',  # 25 Zeichen, 4 Arten
    'H$llo12345678901234567890H$llo12345678901234567890',  # 50 Zeichen, 4 Arten
]


# Liste von ungültigen Passwörtern
invalid_passwords = [
    '1234',  # 4 Zeichen, 1 Art
    '12345678',  # 8 Zeichen, 1 Art
    'Hallo123Hallo123Hallo123',  # 24 Zeichen, 3 Arten
]


@pytest.mark.parametrize("password", valid_passwords)
def test_is_valid_password__gueltige_Passwoerter(password):
    assert is_valid_password(password) is True


@pytest.mark.parametrize("password", invalid_passwords)
def test_is_valid_password__ungueltige_Passwoerter(password):
    assert is_valid_password(password) is False
