from fastapi import FastAPI

from app.config import settings
from app.routers.account import router as account_router
from app.routers.swap import router as swap_router

app = FastAPI()


api_router_config = {"prefix": "/api"}
ws_router_config = {"prefix": "/ws"}

app.include_router(account_router, **api_router_config)  # type: ignore
app.include_router(swap_router, **api_router_config)  # type: ignore


@app.get("/")
async def read_root():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.API_VERSION,
        "description": "API for XRPL-Swap",
        "contact": {
            "email": "jjaa1012@gmail.com",
            "github": "https://github.com/wonj1012",
            "linkedin": "https://www.linkedin.com/in/wonj",
        },
        "docs": "/docs",
        "redoc": "/redoc",
    }
