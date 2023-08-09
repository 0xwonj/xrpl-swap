from fastapi import APIRouter, Depends

from xrpl.asyncio.clients import AsyncJsonRpcClient

from app.xrpl.client import get_xrpl_client
from app.xrpl.request import fetch_account_info

from app.models.types import Address, Result

router = APIRouter(
    prefix="/account",
    tags=["account"],
    dependencies=[Depends(get_xrpl_client)],
    responses={
        400: {"description": "Invalid Request"},
        404: {"description": "Account Not Found"},
    },
)


@router.get("/info/{address}")
async def account_info(
    address: str, client: AsyncJsonRpcClient = Depends(get_xrpl_client)
) -> Result:
    return await fetch_account_info(client=client, address=Address(value=address))
