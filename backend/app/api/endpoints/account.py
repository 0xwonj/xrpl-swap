from fastapi import APIRouter, Depends

from xrpl.asyncio.clients import AsyncJsonRpcClient

from xrpledger.client import get_xrpl_client
from xrpledger.request import fetch_account_info

from models.types import Address, Result

router = APIRouter()


@router.get("/info/{account}")
async def account_info(
    account: str, client: AsyncJsonRpcClient = Depends(get_xrpl_client)
) -> Result:
    return await fetch_account_info(client=client, address=Address(value=account))
