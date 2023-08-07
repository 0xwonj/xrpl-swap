from xrpl.asyncio.clients import AsyncJsonRpcClient

from constants import TESTNET_URL


async def get_xrpl_client() -> AsyncJsonRpcClient:
    """
    Returns an AsyncJsonRpcClient instance connected to the XRPL (XRP Ledger) testnet.

    Returns:
        AsyncJsonRpcClient: An instance of AsyncJsonRpcClient connected to the XRPL testnet.
    """
    return AsyncJsonRpcClient(TESTNET_URL)
