import os
from dotenv import load_dotenv

from xrpl.asyncio.clients import AsyncJsonRpcClient

from constants import TESTNET_URL, MAINNET_URL, AMMDEVNET_URL

load_dotenv()


def get_url() -> str:
    env = os.getenv("XRPL_ENVIRONMENT", "MAINNET")

    return {
        "TESTNET": TESTNET_URL,
        "MAINNET": MAINNET_URL,
        "DEVNET": AMMDEVNET_URL,
    }.get(env, MAINNET_URL)


async def get_xrpl_client(url: str | None = None) -> AsyncJsonRpcClient:
    """
    Returns an AsyncJsonRpcClient instance connected to the XRPL (XRP Ledger) testnet.

    Returns:
        AsyncJsonRpcClient: An instance of AsyncJsonRpcClient connected to the XRPL testnet.
    """
    if url is None:
        url = get_url()
    return AsyncJsonRpcClient(url)
