import pytest
from services import *

def test_password_corta():
    with pytest.raises(PasswordErrorShort):
        validate_password("1234567")

def test_password_sin_numero():
    with pytest.raises(PasswordNoNumberError):
        validate_password("abcdefgh")

def test_password_valida():
    assert validate_password("abcdefg1") == True