from typing import Any

from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.requests import AccountInfo, Request, RipplePathFind

from app.models.types import Amount


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


async def get_exchange_rate(
    source_address: str,
    destination_address: str,
    send_amount: Amount,
    destination_amount: Amount,
    client: AsyncJsonRpcClient,
) -> float | None:
    """
    Args:
        source_address (str): _description_
        destination_address (str): _description_
        send_amount (Amount): _description_
        destination_amount (Amount): _description_
        client (AsyncWebsocketClient, optional): _description_. Defaults to Depends(get_xrpl_ws_client).

    Returns:
        float | None: _description_
    """
    result = await request_ledger(
        request=RipplePathFind(
            source_account=source_address,
            destination_account=destination_address,
            destination_amount=destination_amount.to_xrpl_amount(),
            send_max=send_amount.to_xrpl_amount(),
        ),
        client=client,
    )

    if "alternatives" in result and result["alternatives"]:
        alternative = result["alternatives"][0]
        source_amount = float(alternative["source_amount"]["value"])
        return source_amount

    return None


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

    # Return result as dictionary
    return response.result
