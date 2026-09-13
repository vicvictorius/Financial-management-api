from sqlalchemy.orm import Session

from app.database.models.transaction import Transaction
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate
)

def create_transaction(db:Session, transaction_data:TransactionCreate, user_id:int):
    transaction = Transaction(
        description=transaction_data.description,
        amount=transaction_data.amount,
        type=transaction_data.type,
        category_id=transaction_data.category_id,
        user_id=user_id
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction

def get_transactions(db: Session, user_id: int):
    return (db.query(Transaction).filter(Transaction.user_id == user_id).all())

def get_transaction(db: Session, transaction_id: int, user_id: int):
    return(db.query(Transaction).filter(Transaction.id == transaction_id, Transaction.user_id == user_id).first())

def update_transaction(db:Session, transaction: Transaction, transaction_data: TransactionUpdate):
    update_data = transaction_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)

    return transaction

def delete_transaction(db:Session, transaction:Transaction):
    db.delete(transaction)
    db.commit()

