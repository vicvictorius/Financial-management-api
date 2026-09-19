from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_income: float
    total_expenses: float
    balance: float


class MonthlySummary(BaseModel):
    income: float
    expenses: float
    balance: float


class MonthlyDashboard(BaseModel):
    income: float
    expenses: float
    balance: float


dict[str, MonthlySummary]
