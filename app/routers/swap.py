from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.transactions import Payment, PaymentFlag
from xrpl.wallet import Wallet

from app.models.annotations import XrplAddress, XrplClient
from app.models.requests import PaymentRequest
from app.xrpl.client import get_xrpl_client
from app.xrpl.transaction import submit_transaction

router = APIRouter(
    prefix="/swap",
    tags=["swap"],
    dependencies=[Depends(get_xrpl_client)],
    responses={
        400: {"description": "Invalid Transaction"},
        404: {"description": ""},
    },
)


@router.post("/buy")
async def buy_token(
    request: PaymentRequest,
    account: XrplAddress,
    client: XrplClient,
) -> JSONResponse:
    """
    Process a token purchase on the XRPL.

    Allows a user to buy a specified amount of a token by providing
    the source currency details, including the max value they are
    willing to spend.
    """
    send_max = IssuedCurrencyAmount(
        currency=request.source.currency,
        issuer=request.source.issuer,
        value=request.source.value,
    )
    amount = IssuedCurrencyAmount(
        currency=request.dest.currency,
        issuer=request.dest.issuer,
        value=request.dest.value,
    )

    swap_tx = Payment(account=account, destination=account, send_max=send_max, amount=amount)

    return await submit_transaction(
        transaction=swap_tx,
        client=client,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
    )


@router.post("/sell")
async def sell_token(
    request: PaymentRequest,
    account: XrplAddress,
    client: XrplClient,
) -> JSONResponse:
    """
    Process a token sale on the XRPL with partial payment support.

    Allows a user to sell a specified amount of a token. The function
    supports partial payments, meaning the seller can receive an amount
    less than or equal to the specified `deliver_min` value, depending on
    the market conditions.
    """

    send_max = IssuedCurrencyAmount(
        currency=request.source.currency,
        issuer=request.source.issuer,
        value=request.source.value,
    )
    amount = IssuedCurrencyAmount(
        currency=request.dest.currency,
        issuer=request.dest.issuer,
        value=request.dest.value,
    )
    deliver_min = IssuedCurrencyAmount(
        currency=request.dest.currency,
        issuer=request.dest.issuer,
        value=request.dest.value,
    )

    swap_tx = Payment(
        account=account,
        destination=account,
        send_max=send_max,
        amount=amount,
        deliver_min=deliver_min,
        flags=[PaymentFlag.TF_PARTIAL_PAYMENT],
    )

    return await submit_transaction(
        transaction=swap_tx,
        client=client,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
    )
