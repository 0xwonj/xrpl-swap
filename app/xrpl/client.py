from fastapi.responses import JSONResponse
from xrpl.asyncio.clients import AsyncJsonRpcClient, AsyncWebsocketClient
from xrpl.models.response import Response

from app.common.config import settings


def get_xrpl_client(url: str | None = None) -> AsyncJsonRpcClient:
    """
    Returns an AsyncJsonRpcClient instance connected to the specified XRPL environment.

    Args:
        url (str, optional): The XRPL environment URL. Defaults to the URL obtained via get_url.

    Returns:
        AsyncJsonRpcClient: An instance of AsyncJsonRpcClient connected to the specified XRPL environment.
    """
    return AsyncJsonRpcClient(settings.json_rpc_url if url is None else url)


def get_xrpl_ws_client(url: str | None = None) -> AsyncWebsocketClient:
    """
    Returns an AsyncWebsocketClient instance connected to the specified XRPL environment.

    Args:
        url (str, optional): The XRPL environment URL. Defaults to the URL obtained via get_url.

    Returns:
        AsyncWebsocketClient: An instance of AsyncWebsocketClient connected to the specified XRPL environment.
    """
    return AsyncWebsocketClient(settings.websocket_url if url is None else url)


def create_json_response(response: Response) -> JSONResponse:
    """
    Creates a JSONResponse based on the given response's success status.

    Args:
        response: The response object which has a method 'is_successful'.

    Returns:
        JSONResponse: The response object formatted as a JSON response.
            (status_code) 200: Response successful.
                          400: Response failed.
    """
    # Set status code based on response success
    if response.is_successful():
        status_code = 200
    else:
        status_code = 400

    # Return JSON response
    return JSONResponse(content=response.result, status_code=status_code)
