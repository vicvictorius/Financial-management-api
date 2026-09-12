from fastapi import FastAPI

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