class PasswordErrorShort(Exception):
    def __init__(self):
        super().__init__("La contrasena es demasiado corta.")

class PasswordNoNumberError(Exception):
    def __init__(self):
        super().__init__("La contrasena debe contener al menos un numero.")


def validate_password(password):
    if len(password) < 8:
        raise PasswordErrorShort()
    if not any(c.isdigit() for c in password):
        raise PasswordNoNumberError()
    return True