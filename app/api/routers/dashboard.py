from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.schemas.dashboard import DashboardSummary, MonthlyDashboard
from app.services.dashboard_service import get_dashboard_monthly, get_dashboard_summary

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary", response_model=DashboardSummary)
def dashboard_summary(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_dashboard_summary(db=db, user_id=current_user.id)


@router.get("/monthly", response_model=dict[str, MonthlyDashboard])
def dashboard_monthly(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_dashboard_monthly(db=db, user_id=current_user.id)
