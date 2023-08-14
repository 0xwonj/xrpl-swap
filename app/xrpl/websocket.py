import asyncio
from fastapi import Depends
from xrpl.models import PathFind, PathFindSubcommand
from xrpl.asyncio.clients import AsyncWebsocketClient

from app.common.config import settings
from app.models.types import Amount
from app.xrpl.client import get_xrpl_ws_client


async def listener(client, source_address, destination_address, send_amount, destination_amount):
    async for message in client:
        if "alternatives" in message.result and message.result["alternatives"]:
            alternative = message.result["alternatives"][0]
            source_amount = float(alternative["source_amount"]["value"])
            print(f"Updated exchange rate: {source_amount}")


async def exchange_rate_stream(
    source_address: str,
    destination_address: str,
    send_amount: Amount,
    destination_amount: Amount,
    client: AsyncWebsocketClient = Depends(get_xrpl_ws_client),
) -> None:
    async with client as ws_client:
        asyncio.create_task(
            listener(ws_client, source_address, destination_address, send_amount, destination_amount)
        )

        await ws_client.send(
            PathFind(
                source_account=source_address,
                destination_account=destination_address,
                destination_amount=destination_amount.to_xrpl_amount(),
                send_max=send_amount.to_xrpl_amount(),
                subcommand=PathFindSubcommand.CREATE,
            )
        )

        await asyncio.sleep(5)  # or any other logic you want to perform while listening

    # now, outside of the context, the client is closed.


if __name__ == "__main__":
    asyncio.run(
        exchange_rate_stream(
            settings.wallet.address,
            settings.wallet.address,
            Amount(symbol="XRP", value="10"),
            Amount(symbol="TST", issuer="rP9jPyP5kyvFRb6ZiRghAGw5u8SGAmU4bd", value="25"),
        )
    )
