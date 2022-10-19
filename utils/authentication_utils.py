from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

import persistency
from persistency.persistency_utils import get_db

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'])
SECRET_KEY = '1f23ab2c0cf6a0f3af6c320c9f1962adb112c3f1492a747b0adf740a41ee2b57'
ALGORITHM = "HS256"


def create_hash(plain_password):
    return pwd_context.hash(plain_password)


def verify_hash(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict):
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {'token': token}


def verify_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')


def get_user_info(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        username: str = verify_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')

    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')

    user = persistency.employee_persistency.EmployeePersistency(db).read_by_username(username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')

    return user
