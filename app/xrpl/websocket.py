import asyncio

from xrpl.asyncio.clients import AsyncWebsocketClient
from xrpl.models import PathFind, PathFindSubcommand

from app.models.types import Amount


async def listener(
    client: AsyncWebsocketClient,
    source_address: str,
    destination_address: str,
    send_amount: Amount,
    destination_amount: Amount,
) -> None:
    """
    Listen to messages from an XRPL Websocket client and print the latest exchange rate
    and transaction details when available.

    Args:
        client (AsyncWebsocketClient): The XRPL Websocket client to listen for messages.
        source_address (str): The address of the sender in the transaction.
        destination_address (str): The address of the recipient in the transaction.
        send_amount (Amount): The amount of currency the sender is sending.
        destination_amount (Amount): The amount of currency the recipient will receive.
    """
    async for message in client:
        if "alternatives" in message and message["alternatives"]:
            alternative = message["alternatives"][0]
            source_amount = float(alternative["source_amount"]["value"])
            print(f"Updated exchange rate: {source_amount}")
            print(f"{source_address} -> {destination_address}")
            print(f"{send_amount} -> {destination_amount}")


async def exchange_rate_stream(
    source_address: str,
    destination_address: str,
    send_amount: Amount,
    destination_amount: Amount,
    client: AsyncWebsocketClient,
) -> None:
    """
    Start a stream to listen for the exchange rate between two addresses for a specified amount.
    This function creates a listener task to monitor messages
    and sends a `PathFind` request to the XRPL Websocket.

    Args:
        source_address (str): The address of the sender in the transaction.
        destination_address (str): The address of the recipient in the transaction.
        send_amount (Amount): The amount of currency the sender is sending.
        destination_amount (Amount): The amount of currency the recipient will receive.
        client (AsyncWebsocketClient, optional): The XRPL Websocket client to use.
    """
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
