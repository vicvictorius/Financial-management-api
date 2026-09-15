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


def get_dashboard_monthly(
    db: Session,
    user_id: int
):
    transactions = (
        db.query(Transaction)
        .filter(
            Transaction.user_id == user_id
        )
        .order_by(Transaction.created_at)
        .all()
    )

    monthly_data = {}

    for transaction in transactions:
        month = transaction.created_at.strftime("%Y-%m")

        if month not in monthly_data:
            monthly_data[month] = {
                "income": 0.0,
                "expenses": 0.0,
                "balance": 0.0
            }

        amount = float(transaction.amount)

        if transaction.type == "income":
            monthly_data[month]["income"] += amount

        elif transaction.type == "expense":
            monthly_data[month]["expenses"] += amount

        monthly_data[month]["balance"] = (
            monthly_data[month]["income"]
            - monthly_data[month]["expenses"]
        )

    return monthly_data