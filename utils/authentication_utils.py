
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])
SECRET_KEY = '1f23ab2c0cf6a0f3af6c320c9f1962adb112c3f1492a747b0adf740a41ee2b57'
ALGORITHM = "HS256"


def create_hash(plain_password):
    return pwd_context.hash(plain_password)


def verify_hash(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
