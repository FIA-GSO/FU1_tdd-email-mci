from email_validator import validate_email, EmailNotValidError


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    try:
      # validate and get info
        v = validate_email(email, check_deliverability=False,
                           allow_smtputf8=False,
                           allow_quoted_local=True,
                           allow_domain_literal=True,
                           test_environment=True)
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        return False
