from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.database.models.user import User


def create_user(db: Session, username: str, email: str, password: str):

    existing_user = (
        db.query(User)
        .filter(
            (User.username == username) | (User.email == email)
        )
        .first()
    )

    if existing_user:
        return None

    password_hash = hash_password(password)

    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
