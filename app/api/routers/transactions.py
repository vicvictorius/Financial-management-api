from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.transaction import(
    TransactionUpdate,
    TransactionCreate,
    TransactionResponse
)

from app.services.transaction_service import(
    create_transaction,
    get_transactions,
    get_transaction,
    update_transaction,
    delete_transaction
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# utilizando user_id = 1 temporariamente, ate integrar auth (JWT)

@router.post(
    "/",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED
)
def create(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    user_id = 1
    return create_transaction(db, transaction_data, user_id)


@router.get(
    "/",
    response_model=list[TransactionResponse]
)
def list_transactions(db: Session = Depends(get_db)):
    user_id = 1
    return get_transactions(db, user_id)


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def get_by_id(transaction_id: int, db: Session = Depends(get_db)):
    user_id = 1

    transaction = get_transaction(db, transaction_id, user_id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return transaction


@router.put(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def update(transaction_id: int, transaction_data: TransactionUpdate, db: Session = Depends(get_db)):
    user_id = 1

    transaction = get_transaction(db, transaction_id, user_id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return update_transaction(db, transaction, transaction_data)


@router.delete(
    "/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(transaction_id: int, db: Session = Depends(get_db)):
    user_id = 1

    transaction = get_transaction(db, transaction_id, user_id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    delete_transaction(db, transaction)