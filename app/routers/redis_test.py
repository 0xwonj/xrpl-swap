from typing import Annotated

from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse

from app.models.annotations import Redis
from database.redis import get_redis

router = APIRouter(
    prefix="/redis",
    tags=["redis"],
    dependencies=[Depends(get_redis)],
)


@router.get("/{key}")
async def get_item(key: Annotated[str, Path()], cache: Redis) -> JSONResponse:
    """
    Get item from Redis cache
    """
    # Get data from Redis cache
    data: str | None = await cache.get(key)

    # Set status code to 200 if data is not None, otherwise set to 404
    status_code = 200 if data else 404

    return JSONResponse(content={key: data}, status_code=status_code)


@router.post("/{key}={value}")
async def set_item(key: Annotated[str, Path()], value: Annotated[str, Path()], cache: Redis) -> JSONResponse:
    """
    Set item in Redis cache
    """
    # Set item in Redis cache
    result = await cache.set(key, value)

    if result:
        status_code = 200
        msg = "Item set successfully"
    else:
        status_code = 500
        msg = "Failed to set item in Redis"

    return JSONResponse(content={"result": msg}, status_code=status_code)
