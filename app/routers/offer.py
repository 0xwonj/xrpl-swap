from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse

from app.models import Redis
from database.redis import get_redis
from etl.offer.read import get_quality
from xrpledger.models import Token

router = APIRouter(
    prefix="/offer",
    tags=["offer"],
    dependencies=[Depends(get_redis)],
)


@router.post("/quality")
async def get_offer_quality(
    token_from: Annotated[Token, Body()],
    token_to: Annotated[Token, Body()],
    from_amount: Annotated[float, Body()],
    redis: Redis,
) -> JSONResponse:
    """
    Get offer quality from Redis
    """
    # Get quality from Redis
    quality = await get_quality((token_from, token_to), from_amount, redis=redis)

    status_code = 200 if (quality > 0) else 404

    return JSONResponse(content={"quality": quality}, status_code=status_code)
