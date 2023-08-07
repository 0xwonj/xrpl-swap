from fastapi import FastAPI
from api.endpoints.account import router as account_router

app = FastAPI()

app.include_router(
    account_router,
    prefix="/api/v1/account",
    tags=["account"],
    responses={404: {"description": "Not found"}},
)
