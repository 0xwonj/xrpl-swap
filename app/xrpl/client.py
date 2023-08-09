import os

from dotenv import load_dotenv
from xrpl.asyncio.clients import AsyncJsonRpcClient

from app.constants import AMMDEVNET_URL, MAINNET_URL, TESTNET_URL

load_dotenv()


def get_url() -> str:
    """
    Determines the XRPL environment URL based on the XRPL_ENVIRONMENT environment variable.

    Returns:
        str: The XRPL environment URL. Returns MAINNET_URL if XRPL_ENVIRONMENT is not set.
    """
    env = os.getenv("XRPL_ENVIRONMENT", "MAINNET")

    return {
        "TESTNET": TESTNET_URL,
        "MAINNET": MAINNET_URL,
        "DEVNET": AMMDEVNET_URL,
    }.get(env, MAINNET_URL)


async def get_xrpl_client(url: str | None = None) -> AsyncJsonRpcClient:
    """
    Returns an AsyncJsonRpcClient instance connected to the specified XRPL environment.

    Args:
        url (str, optional): The XRPL environment URL. Defaults to the URL obtained via get_url.

    Returns:
        AsyncJsonRpcClient: An instance of AsyncJsonRpcClient connected to the specified XRPL environment.
    """
    if url is None:
        url = get_url()
    return AsyncJsonRpcClient(url)
