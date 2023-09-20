from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator

from app.models import Redis
from database.redis import get_redis
from etl.offer.read import get_quality
from xrpledger.data.tokens import tokens
from xrpledger.models import Token

router = APIRouter(
    prefix="/offer",
    tags=["offer"],
    dependencies=[Depends(get_redis)],
)


class OfferQualityRequest(BaseModel):
    """
    A model representing the request for a token swap.
    """

    token_from: Annotated[
        Token, Field(..., description="The source token for the swap", example=tokens["XRP"])
    ]
    token_to: Annotated[
        Token, Field(..., description="The destination token for the swap", example=tokens["USD.Gatehub"])
    ]
    from_amount: Annotated[float, Field(..., ge=0, description="The source token amount for the swap")]

    @validator("token_to", pre=True, always=True)
    def validate_token_pair(cls, token_to: Token, values: dict) -> Token:
        """
        Validate token pair
        """
        token_from = values.get("token_from")
        if token_from == token_to:
            raise ValueError("token_from and token_to should be different")
        return token_to


@router.post("/quality")
async def get_offer_quality(
    request: OfferQualityRequest,
    redis: Redis,
) -> JSONResponse:
    """
    Get offer quality from Redis
    """
    # Get quality from Redis
    quality = await get_quality((request.token_from, request.token_to), request.from_amount, redis=redis)

    status_code = 200 if (quality > 0) else 404

    return JSONResponse(content=quality, status_code=status_code)
