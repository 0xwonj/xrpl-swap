from fastapi import APIRouter, Depends
from xrpl.asyncio.clients import AsyncJsonRpcClient

from app.config import settings
from app.models.types import Address, Result
from app.xrpl.client import get_xrpl_client
from app.xrpl.request import fetch_account_info

router = APIRouter(
    prefix="/account",
    tags=["account"],
    dependencies=[Depends(get_xrpl_client)],
    responses={
        400: {"description": "Invalid Request"},
        404: {"description": "Account Not Found"},
    },
)


@router.get("/info/{account}")
async def get_account_info(
    account: str = settings.wallet.address.value, client: AsyncJsonRpcClient = Depends(get_xrpl_client)
) -> Result:
    """
    Fetches the account information for a given XRPL address.

    Args:
        account (str): The XRPL address for which the account information is to be fetched.
        client (AsyncJsonRpcClient, optional): Client to connect to the XRPL.
                                               Defaults to a client obtained via get_xrpl_client.

    Returns:
        Result: A Result object containing the account information.
    """
    return await fetch_account_info(client=client, address=Address(value=account))
