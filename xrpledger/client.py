from xrpl.asyncio.clients import AsyncJsonRpcClient, AsyncWebsocketClient

from common.config import settings


def get_xrpl_rpc_client(url: str | None = None) -> AsyncJsonRpcClient:
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
