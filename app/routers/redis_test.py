from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.models.annotations import Redis
from app.database.redis import get_redis

router = APIRouter(
    prefix="/redis",
    tags=["redis"],
    dependencies=[Depends(get_redis)],
)


@router.post("/foo")
async def set_foo_bar(cache: Redis) -> None:
    await cache.set("foo", "bar")


@router.get("/foo")
async def get_foo(cache: Redis) -> JSONResponse:
    data = await cache.get("foo")

    if data:
        data = data.decode("utf-8")

    return JSONResponse(content={"foo": data}, status_code=200)
