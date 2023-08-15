from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.database.redis import get_redis
from app.models.annotations import Redis

router = APIRouter(
    prefix="/redis",
    tags=["redis"],
    dependencies=[Depends(get_redis)],
)


@router.get("/{key}")
async def get_item(key: str, cache: Redis) -> JSONResponse:
    """
    Get item from Redis cache
    """
    data: bytes = await cache.get(key)

    if data is None:
        status_code = 404
        result = "Not Found"
    else:
        status_code = 200
        result = data.decode("utf-8")

    return JSONResponse(content={key: result}, status_code=status_code)


@router.post("/{key}={value}")
async def set_item(key: str, value: str, cache: Redis) -> JSONResponse:
    """
    Set item in Redis cache
    """
    result = await cache.set(key, value)

    if result:
        status_code = 200
        data = "Item set successfully"
    else:
        status_code = 500
        data = "Failed to set item in Redis"

    return JSONResponse(content={"result": data}, status_code=status_code)
