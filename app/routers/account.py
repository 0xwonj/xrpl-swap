from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.models.annotations import XrplAddress, XrplClient
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


@router.get("/{account}/info")
async def get_account_info(
    account: XrplAddress,
    client: XrplClient,
) -> JSONResponse:
    """
    Fetches the account information for a given XRPL address.
    """
    return await fetch_account_info(client=client, address=account)
