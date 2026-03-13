class PasswordErrorShort(Exception):
    def __init__(self):
        super().__init__("La contrasena es demasiado corta.")

class PasswordNoNumberError(Exception):
    def __init__(self):
        super().__init__("La contrasena debe contener al menos un numero.")
        
class PasswordNoCaracterError(Exception):
    def __init__(self):
        super().__init__("La contrasena debe contener al menos un caracter.")

class PasswordNoMayusError(Exception):
    def __init__(self):
        super().__init__("La contrasena debe contener al menos una letra en mayuscula.")

class PasswordNoMinusError(Exception):
    def __init__(self):
        super().__init__("La contrasena debe contener al menos una letra en minuscula.")

class PasswordNoSpecialCharError(Exception):
    def __init__(self):
        super().__init__("La contrasena debe contener al menos un caracter especial.")

def validate_password(password):
    if len(password) < 8:
        raise PasswordErrorShort()
    if not any(c.isdigit() for c in password):
        raise PasswordNoNumberError()
    if not any(c.isalpha() for c in password):
        raise PasswordNoCaracterError()
    if not any(c.isupper() for c in password):
        raise PasswordNoMayusError()
    if not any(c.islower() for c in password):
        raise PasswordNoMinusError()
    if not any(not c.isalnum() for c in password):
        raise PasswordNoSpecialCharError()
    return True