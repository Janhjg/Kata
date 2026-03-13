import pytest
from services import *

def test_password_corta():
    with pytest.raises(PasswordErrorShort):
        validate_password("1234567")

def test_password_sin_numero():
    with pytest.raises(PasswordNoNumberError):
        validate_password("abcdefgh")

def test_password_sin_caracter():
    with pytest.raises(PasswordNoCaracterError):
        validate_password("12345678")
        
def test_password_sin_mayus():
    with pytest.raises(PasswordNoMayusError):
        validate_password("1234nnnn")
        
def test_password_sin_minus():
    with pytest.raises(PasswordNoMinusError):
        validate_password("1234AAAA")
        
def test_password_sin_especial():
    with pytest.raises(PasswordNoSpecialCharError):
        validate_password("Abcdefg1")

def test_password_valida():
    assert validate_password("Abcdefg1!") == True