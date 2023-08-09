from fastapi import APIRouter, Depends
from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.transactions import Payment, PaymentFlag
from xrpl.wallet import Wallet

from app.models.requests import TokenSwapRequest
from app.models.types import Result
from app.xrpl.client import get_xrpl_client
from app.xrpl.transaction import submit_transaction
from app.config import settings

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
    request: TokenSwapRequest,
    account: str = settings.wallet.address.value,
    client: AsyncJsonRpcClient = Depends(get_xrpl_client),
) -> Result:
    """
    Process a token purchase on the XRPL.

    Allows a user to buy a specified amount of a token by providing
    the source currency details, including the max value they are
    willing to spend.

    Args:
        account (str): XRPL account address initiating the purchase.
        request (TokenSwapRequest): Request data specifying the source
            currency details and the desired token's details.
        client (AsyncJsonRpcClient, optional): XRPL client instance for
            interacting with the XRPL network. Defaults to an instance
            created by `get_xrpl_client`.

    Returns:
        Result: Result of the token purchase transaction, including
            transaction details and status.
    """
    send_max = IssuedCurrencyAmount(
        currency=request.source.currency,
        issuer=request.source.issuer,
        value=request.source.value,  # This is the max amount to spend
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
    request: TokenSwapRequest,
    account: str = settings.wallet.address.value,
    client: AsyncJsonRpcClient = Depends(get_xrpl_client),
) -> Result:
    """
    Process a token sale on the XRPL with partial payment support.

    Allows a user to sell a specified amount of a token. The function
    supports partial payments, meaning the seller can receive an amount
    less than or equal to the specified `deliver_min` value, depending on
    the market conditions.

    Args:
        account (str): XRPL account address initiating the sale.
        request (TokenSwapRequest): Request data specifying the source
            token's details and the desired destination currency details.
        client (AsyncJsonRpcClient, optional): XRPL client instance for
            interacting with the XRPL network. Defaults to an instance
            created by `get_xrpl_client`.

    Returns:
        Result: Result of the token sale transaction, including
            transaction details and status.
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
