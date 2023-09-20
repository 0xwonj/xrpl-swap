from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers.account import router as account_router
from app.routers.orderbook import router as orderbook_router
from app.routers.redis_test import router as redis_router
from app.routers.payment import router as swap_router
from common.config import settings

app = FastAPI()

origins = [
    "http://localhost:4427",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router_config = {"prefix": "/api"}
ws_router_config = {"prefix": "/ws"}

app.include_router(account_router, **api_router_config)  # type: ignore
app.include_router(swap_router, **api_router_config)  # type: ignore
app.include_router(redis_router, **api_router_config)  # type: ignore
app.include_router(orderbook_router, **api_router_config)  # type: ignore


@app.get("/")
async def read_root(request: Request) -> JSONResponse:
    """
    Root endpoint for the API.
    """
    base_url = str(request.base_url)

    return JSONResponse(
        status_code=200,
        content={
            "name": settings.PROJECT_NAME,
            "version": settings.API_VERSION,
            "description": "API for XRPL-Swap",
            "contact": {
                "email": "choi@wonj.me",
                "github": "https://github.com/Helix-Organization/xrpl-swap",
            },
            "docs": f"{base_url}docs",
            "redoc": f"{base_url}redoc",
        },
    )
