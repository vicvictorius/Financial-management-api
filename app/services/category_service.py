from sqlalchemy.orm import Session

from app.database.models.category import Category


def create_category(db: Session, name: str):

    existing_category = db.query(Category).filter(Category.name == name).first()

    if existing_category:
        return None

    category = Category(name=name)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(db: Session):

    return db.query(Category).all()


def get_category(db: Session, category_id: int):

    return db.query(Category).filter(Category.id == category_id).first()
