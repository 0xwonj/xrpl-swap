from xrpl.clients import XRPLRequestFailureException
from xrpl.models.requests import Request
from xrpl.asyncio.clients import AsyncJsonRpcClient

from models.types import Result


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
