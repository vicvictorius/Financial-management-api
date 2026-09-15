from fastapi import FastAPI

from app.api.routers import auth
from app.database.database import Base, engine
from app.database.models import user, category
from app.api.routers import categories
from app.api.routers.transactions import router as transaction_router
from app.api.routers.dashboard import router as dashboard_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Financial Management API",
    description="API para gerenciamento financeiro pessoal",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Financial Management API is running!!"
    }


app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(transaction_router)
app.include_router(dashboard_router)
