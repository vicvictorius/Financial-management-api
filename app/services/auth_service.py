from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.database.models.user import User


def create_user(db: Session, username: str, email: str, password: str):

    password_hash = hash_password(password)

    user = User(username=username, email=email, password_hash=password_hash)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
