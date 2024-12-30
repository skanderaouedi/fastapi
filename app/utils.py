from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_pass(password: str) -> str:
    return ph.hash(password)

from argon2.exceptions import VerifyMismatchError

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError:
        return False