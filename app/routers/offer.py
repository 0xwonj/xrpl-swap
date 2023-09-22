from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from xrpl.models.transactions import OfferCancel, OfferCreate, OfferCreateFlag
from xrpl.wallet import Wallet

from app.models import (
    OfferCancelRequest,
    OfferCreateRequest,
    OfferQualityRequest,
    Redis,
    XrplClient,
)
from database.redis import get_redis
from etl.offer.read import get_quality
from xrpledger.transaction import submit_transaction

router = APIRouter(
    prefix="/offer",
    tags=["offer"],
    dependencies=[Depends(get_redis)],
)


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


@router.post("/create")
async def offer_create(request: OfferCreateRequest, client: XrplClient) -> JSONResponse:
    """
    Process Offer Create on XRPL Orderbook.
    """
    transaction = OfferCreate(
        account=request.account,
        taker_pays=request.taker_pays.to_xrpl_amount(),
        taker_gets=request.taker_gets.to_xrpl_amount(),
        flags=OfferCreateFlag.TF_SELL,
    )

    result = await submit_transaction(
        transaction=transaction,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
        client=client,
    )

    status_code = 400 if "error" in result else 200

    return JSONResponse(content=result, status_code=status_code)


@router.post("/cancel")
async def offer_cancel(request: OfferCancelRequest, client: XrplClient) -> JSONResponse:
    """
    Process Offer Create on XRPL Orderbook.
    """
    transaction = OfferCancel(account=request.account, offer_sequence=request.offer_sequence)

    result = await submit_transaction(
        transaction=transaction,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
        client=client,
    )

    status_code = 400 if "error" in result else 200

    return JSONResponse(content=result, status_code=status_code)
