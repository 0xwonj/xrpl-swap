from typing import Any

from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.requests import AccountInfo, Request

from app.xrpl.client import create_json_response


async def fetch_account_info(address: str, client: AsyncJsonRpcClient, **kwargs: Any) -> dict[str, Any]:
    """
    Fetches account information asynchronously from the XRPL network.

    Args:
        client (AsyncJsonRpcClient): The client to send the request.
        address (str): The address of the account to fetch the information from.
        **kwargs: Optional arguments to be added to the `AccountInfo` request.

    Returns:
        JSONResponse: An instance of JSONResponse object containing the information of this account.
            (status_code) 200: Request successful.
                          400: Request failed.
    """
    return await request_ledger(request=AccountInfo(account=address, **kwargs), client=client)


async def request_ledger(request: Request, client: AsyncJsonRpcClient) -> dict[str, Any]:
    """
    Sends a ledger request to the XRPL (XRP Ledger) network asynchronously.

    Args:
        client (AsyncJsonRpcClient): Async JSON RPC client for XRP Ledger.
        request (Request): An instance of Request representing the ledger request to be sent.

    Returns:
        JSONResponse: An instance of JSONResponse object containing the response data from the request.
            (status_code) 200: Request successful.
                          400: Request failed.
    """
    # Send request and get response
    response = await client.request(request)

    return response.result
