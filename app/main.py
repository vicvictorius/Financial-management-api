import time

from fastapi import FastAPI
from prometheus_client import make_asgi_app

from app.api.routers import auth, categories
from app.api.routers.dashboard import router as dashboard_router
from app.api.routers.health import router as health_router
from app.api.routers.transactions import router as transaction_router
from app.core.metrics import REQUEST_COUNT, REQUEST_DURATION

app = FastAPI(
    title="Financial Management API",
    description="API para gerenciamento financeiro pessoal",
    version="1.0.0",
)


@app.middleware("http")
async def metrics_middleware(request, call_next):
    if request.url.path == "/metrics":
        return await call_next(request)

    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        status_code=str(response.status_code),
    ).inc()

    REQUEST_DURATION.labels(
        method=request.method,
    ).observe(duration)

    return response


app.mount("/metrics", make_asgi_app())


@app.get("/")
def root():
    return {"message": "Financial Management API is running!!"}


app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(transaction_router)
app.include_router(dashboard_router)
app.include_router(health_router)
