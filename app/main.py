from fastapi import FastAPI

from app.database.database import Base, engine
from app.database.models import user
from app.routers import auth


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