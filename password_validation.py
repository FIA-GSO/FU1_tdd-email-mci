def is_valid_password(password: str) -> bool:
    def count_char_types(password: str) -> int:
        char_types = 0
        if any(c.isupper() for c in password):
            char_types += 1
        if any(c.islower() for c in password):
            char_types += 1
        if any(c.isdigit() for c in password):
            char_types += 1
        if any(not c.isalnum() for c in password):
            char_types += 1
        return char_types

    if len(password) >= 8 and count_char_types(password) >= 4:
        return True
    elif len(password) >= 25 and count_char_types(password) >= 2:
        return True

    return False
