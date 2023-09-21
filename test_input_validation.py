import pytest
from input_validation import is_valid_email

valid_emails = [
    'email@example.com',
    'firstname.lastname@example.com',
    'email@subdomain.example.com',
    'firstname+lastname@example.com',
    # 'email@123.123.123.123',
    'email@[123.123.123.123]',
    '"email"@example.com',
    '1234567890@example.com',
    'email@example-one.com',
    '_______@example.com',
    'email@example.name',
    'email@example.museum',
    'email@example.co.jp',
    'firstname-lastname@example.com',
    # 'much."more\ unusual"@example.com',
    # 'very.unusual."@".unusual.com@example.com',
    # 'very."(),:;<>[]".VERY."very@\\\ ',
    # '\"very".unusual@strange.example.com',
]  # einige auskommentiert, weil Python die backslashes nicht richtig escaped - beim nächsten mal lege ich die Mail-Adressen in eine separate File ab und lade sie daraus

invalid_emails = [
    'plainaddress',
    '#@%^%#$@#$@#.com',
    '@example.com',
    'Joe Smith <email@example.com>',
    'email.example.com',
    'email@example@example.com',
    '.email@example.com',
    'email.@example.com',
    'email..email@example.com',
    'あいうえお@example.com',
    'email@example.com (Joe Smith)',
    'email@example',
    'email@-example.com',
    # 'email@example.web',  # .web is not valid TLD
    'email@111.222.333.44444',
    'email@example..com',
    'Abc..123@example.com',
]


@pytest.mark.parametrize("email", valid_emails)
def test_is_valid_email__gueltige_Adressen(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize("email", invalid_emails)
def test_is_valid_email__ungueltige_Adressen(email):
    assert is_valid_email(email) is False
