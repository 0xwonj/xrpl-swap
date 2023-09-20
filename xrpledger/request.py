from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.requests import AccountInfo, BookOffers, Request

from xrpledger.models import Token


async def fetch_account_info(address: str, client: AsyncJsonRpcClient, **kwargs: any) -> dict[str, any]:
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


async def get_orderbook(
    taker_gets: Token,
    taker_pays: Token,
    client: AsyncJsonRpcClient,
    limit: int | None = None,
    taker: str | None = None,
) -> dict[str, any]:
    """
    Args:
        taker_gets (Token): _description_
        taker_pays (Token): _description_
        client (AsyncWebsocketClient, optional): _description_. Defaults to Depends(get_xrpl_ws_client).

    Returns:
        dict[str, any]: _description_
    """
    return await request_ledger(
        request=BookOffers(
            taker_gets=taker_gets.to_xrpl_currency(),
            taker_pays=taker_pays.to_xrpl_currency(),
            limit=limit,
            taker=taker,
        ),
        client=client,
    )


async def request_ledger(request: Request, client: AsyncJsonRpcClient) -> dict[str, any]:
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
