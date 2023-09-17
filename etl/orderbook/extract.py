from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpledger.request import get_orderbook
from xrpledger.models import Token


async def extract_orderbook(
    taker_gets: Token,
    taker_pays: Token,
    client: AsyncJsonRpcClient,
) -> dict[str, any]:
    """
    Args:
        taker_gets (Amount): _description_
        taker_pays (Amount): _description_
        client (AsyncWebsocketClient, optional): _description_. Defaults to Depends(get_xrpl_ws_client).

    Returns:
        dict[str, Any]: _description_
    """
    orderbook_info = await get_orderbook(taker_gets, taker_pays, client)

    offers = orderbook_info["offers"]

    return offers
