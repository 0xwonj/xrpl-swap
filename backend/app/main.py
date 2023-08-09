from fastapi import FastAPI
from api.endpoints.account import router as account_router
from api.endpoints.swap import router as swap_router

app = FastAPI()


api_router_config = {"prefix": "/api"}
ws_router_config = {"prefix": "/ws"}

app.include_router(account_router, **api_router_config)  # type: ignore
app.include_router(swap_router, **api_router_config)  # type: ignore
