from sqlalchemy import Column, Interger, String, DataTime
from sqlaclchemy.sql import func

from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(
        Interger,
        primary_key=True,
        index=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DataTime(timezone=True),
        server_default=func.now()
    )