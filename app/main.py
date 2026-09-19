from fastapi import FastAPI

from app.api.routers import auth, categories
from app.api.routers.dashboard import router as dashboard_router
from app.api.routers.health import router as health_router
from app.api.routers.transactions import router as transaction_router

app = FastAPI(
    title="Financial Management API",
    description="API para gerenciamento financeiro pessoal",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Financial Management API is running!!"}


app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(transaction_router)
app.include_router(dashboard_router)
app.include_router(health_router)
