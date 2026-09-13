from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os

from dotenv import load_dotenv

load_dotenv()

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITM = os.getenv("ALGORITM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","30"))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str,password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

def create_access_token(user_id: int):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITM)


# Funcionamento do fluxo: senha -> bcrypt -> password_hash -> PostgreSQL
