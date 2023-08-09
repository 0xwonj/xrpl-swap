from xrpl.asyncio.clients import AsyncJsonRpcClient

from app.config import settings


async def get_xrpl_client(url: str | None = None) -> AsyncJsonRpcClient:
    """
    Returns an AsyncJsonRpcClient instance connected to the specified XRPL environment.

    Args:
        url (str, optional): The XRPL environment URL. Defaults to the URL obtained via get_url.

    Returns:
        AsyncJsonRpcClient: An instance of AsyncJsonRpcClient connected to the specified XRPL environment.
    """
    return AsyncJsonRpcClient(settings.json_rpc_url if url is None else url)
