from fastapi import APIRouter, Depends

from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.transactions import Payment
from xrpl.wallet import Wallet

from xrpledger.client import get_xrpl_client
from xrpledger.transaction import submit_transaction

from models.types import Result
from models.requests import TokenSwapRequest

router = APIRouter(
    prefix="/swap",
    tags=["swap"],
    dependencies=[Depends(get_xrpl_client)],
    responses={
        400: {"description": "Invalid Transaction"},
        404: {"description": ""},
    },
)


@router.post("/execute")
async def swap_token(
    account: str,
    request: TokenSwapRequest,
    client: AsyncJsonRpcClient = Depends(get_xrpl_client),
) -> Result:
    source_amount = IssuedCurrencyAmount(
        currency=request.source.currency,
        issuer=request.source.issuer,
        value=request.source.value,
    )
    dest_amount = IssuedCurrencyAmount(
        currency=request.dest.currency,
        issuer=request.dest.issuer,
        value=request.dest.value,
    )

    swap_tx = Payment(
        account=account, destination=account, send_max=source_amount, amount=dest_amount
    )

    return await submit_transaction(
        transaction=swap_tx,
        client=client,
        wallet=Wallet(public_key=request.public, private_key=request.secret),
    )
