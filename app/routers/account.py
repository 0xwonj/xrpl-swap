from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.models.annotations import XrplAddress, XrplClient
from app.models.responses import AccountInfoResponse
from app.xrpl.client import get_xrpl_client
from app.xrpl.request import fetch_account_info

router = APIRouter(
    prefix="/account",
    tags=["account"],
    dependencies=[Depends(get_xrpl_client)],
    responses={"400": {"description": "Request failed"}},
)


@router.get("/{account}/info", response_model=AccountInfoResponse)
async def get_account_info(
    account: XrplAddress,
    client: XrplClient,
) -> JSONResponse:
    """
    Fetches the account information for a given XRPL address.
    """
    result = await fetch_account_info(address=account, client=client)

    status_code = 400 if "error" in result else 200

    return JSONResponse(content=result, status_code=status_code)
