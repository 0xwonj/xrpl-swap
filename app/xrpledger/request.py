from typing import Any
from xrpl.clients import XRPLRequestFailureException
from xrpl.models.requests import Request, AccountInfo
from xrpl.asyncio.clients import AsyncJsonRpcClient

from models.types import Address, Result


async def fetch_account_info(
    client: AsyncJsonRpcClient, address: Address, **kwargs: Any
) -> Result:
    """
    Fetches account information asynchronously from the XRPL network.

    Args:
        client (AsyncJsonRpcClient): The client to send the request.
        address (Address): The address of the account to fetch the information from.
        **kwargs: Optional arguments to be added to the `AccountInfo` request.

    Returns:
        Result: A Result object containing the information of this account.

    Raises:
        XRPLRequestFailureException: If the request fails.

    Example:
        >>> async with AsyncJsonRpcClient(url) as client:
        >>>     result = await fetch_account_info(client, Address('rSomeAddress'), ledger_index='current')
    """

    return await request_ledger(client, AccountInfo(account=address.value, **kwargs))


async def request_ledger(client: AsyncJsonRpcClient, request: Request) -> Result:
    """
    Sends a ledger request to the XRPL (XRP Ledger) network asynchronously.

    This function performs an asynchronous communication with the XRPL network. It takes a request object
    and forwards it to the network using the provided AsyncJsonRpcClient. The result of the request is
    encapsulated and returned in a Result object.

    Args:
        client (AsyncJsonRpcClient): The AsyncJsonRpcClient instance used to send the request.
        request (Request): An instance of Request representing the ledger request to be sent.

    Returns:
        Result: An instance of Result object containing the response data from the request.

    Raises:
        XRPLRequestFailureException: Raised when the request to XRPL network fails. Contains additional
        information about the failed request.

    Note:
        This function is a coroutine, it should be run inside an asyncio event loop as
        'await send_ledger_request(...)'.
    """

    # Send request and get response
    response = await client.request(request)

    # Raise exception if request failed
    if not response.is_successful():
        raise XRPLRequestFailureException(response.result)

    # Return result
    return Result(data=response.result)
