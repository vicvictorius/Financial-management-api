from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.models.transaction import Transaction


def get_dashboard_summary(
    db: Session,
    user_id: int
):
    total_income = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.user_id == user_id,
            Transaction.type == "income"
        )
        .scalar()
    )

    total_expenses = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.user_id == user_id,
            Transaction.type == "expense"
        )
        .scalar()
    )

    balance = total_income - total_expenses

    return {
        "total_income": float(total_income),
        "total_expenses": float(total_expenses),
        "balance": float(balance)
    }