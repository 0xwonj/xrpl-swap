from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from xrpl.models.transactions import Payment
from xrpl.wallet import Wallet

from app.models.annotations import XrplClient
from app.models.requests import PaymentRequest
from app.xrpl.client import get_xrpl_client
from app.xrpl.transaction import submit_transaction

router = APIRouter(
    prefix="/swap",
    tags=["swap"],
    dependencies=[Depends(get_xrpl_client)],
)


@router.post("/send")
async def send_token(request: PaymentRequest, client: XrplClient) -> JSONResponse:
    """
    Process a token send on the XRPL. Token is including XRP.

    send_max and destination token should be the same.

    Allows a user to send a specified amount of a token to another
    XRPL address.
    """
    if request.send_max and (
        request.send_max.symbol,
        request.send_max.issuer,
    ) != (
        request.amount.symbol,
        request.amount.issuer,
    ):
        raise HTTPException(status_code=422, detail="send_max and destination tokens should be the same.")

    if request.account == request.destination:
        raise HTTPException(status_code=422, detail="source and destination should be the different.")

    transaction = Payment(
        account=request.account,
        destination=request.destination,
        amount=request.amount.to_xrpl_amount(),
        send_max=request.send_max.to_xrpl_amount() if request.send_max else None,
    )

    return await submit_transaction(
        transaction=transaction,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
        client=client,
    )


@router.post("/swap")
async def swap_token(
    request: PaymentRequest,
    client: XrplClient,
) -> JSONResponse:
    """
    Process a token purchase on the XRPL.

    Allows a user to buy a specified amount of a token by providing
    the send_max currency details, including the max value they are
    willing to spend.
    """
    if request.send_max and (
        request.send_max.symbol,
        request.send_max.issuer,
    ) == (
        request.amount.symbol,
        request.amount.issuer,
    ):
        raise HTTPException(
            status_code=422, detail="send_max and destination tokens should be the different."
        )

    if request.account != request.destination:
        raise HTTPException(status_code=422, detail="source and destination should be the same.")

    transaction = Payment(
        account=request.account,
        destination=request.destination,
        amount=request.amount.to_xrpl_amount(),
        send_max=request.send_max.to_xrpl_amount() if request.send_max else None,
        deliver_min=request.deliver_min.to_xrpl_amount() if request.deliver_min else None,
    )

    return await submit_transaction(
        transaction=transaction,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
        client=client,
    )
