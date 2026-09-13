from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import (
    create_category,
    get_categories,
    get_category
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post(
    "/",
    response_model=CategoryResponse
)
def create(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):

    new_category = create_category(
        db,
        category.name
    )

    if not new_category:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )

    return new_category


@router.get(
    "/",
    response_model=list[CategoryResponse]
)
def list_all(
    db: Session = Depends(get_db)
):
    return get_categories(db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
def get_by_id(
    category_id: int,
    db: Session = Depends(get_db)
):

    category = get_category(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category