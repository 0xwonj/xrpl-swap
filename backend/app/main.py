from fastapi import FastAPI
from api.endpoints.account import router as account_router

app = FastAPI()


common_router_config = {"prefix": "/api/v1"}

app.include_router(account_router, **common_router_config)  # type: ignore
