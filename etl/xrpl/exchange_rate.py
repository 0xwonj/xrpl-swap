from typing import Optional

from xrpl.asyncio.clients import AsyncWebsocketClient
from xrpl.models import PathFind, PathFindSubcommand

from xrpledger.models import Amount


async def exchange_rate_stream(
    source_address: str,
    destination_address: str,
    destination_amount: Amount,
    client: AsyncWebsocketClient,
    source_amount: Optional[Amount] = None,
) -> None:
    """
    Request the XRPL Websocket for possible paths and their exchange rates between
    the given source and destination addresses for a specified amount.
    """
    await client.send(
        PathFind(
            source_account=source_address,
            destination_account=destination_address,
            destination_amount=destination_amount.to_xrpl_amount(),
            send_max=source_amount.to_xrpl_amount() if source_amount else None,
            subcommand=PathFindSubcommand.CREATE,
        )
    )


async def listener(client: AsyncWebsocketClient) -> None:
    """
    Continuously listen to and process messages from an XRPL Websocket client.
    """
    handlers = {
        "response": handle_response,
        "path_find": handle_path_find,
        "error": handle_unexpected,
    }

    async for message in client:
        handler = handlers.get(message["type"], handlers["error"])
        await handler(message)


# Message Handlers
async def handle_response(message: dict) -> None:
    """
    Handle 'response' message types.
    """
    print(message)


async def handle_path_find(message: dict) -> None:
    """
    Handle 'path_find' message types.
    """
    if not message["alternatives"]:
        print("No path found")
        return

    source_amount = float(message["alternatives"][0]["source_amount"])
    dest_amount_value = float(message["destination_amount"]["value"])
    exchange_rate = source_amount / dest_amount_value
    print(exchange_rate)


async def handle_unexpected(message: dict) -> None:
    """
    Handle unexpected message types.
    """
    raise Exception(f"Unexpected message type: {message['type']}")  # pylint: disable=W0719
