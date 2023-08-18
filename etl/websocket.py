import asyncio
from typing import Optional

from xrpl.asyncio.clients import AsyncWebsocketClient
from xrpl.models import PathFind, PathFindSubcommand

from app.models.types import Amount
from app.xrpl.client import get_xrpl_ws_client


async def listener(
    client: AsyncWebsocketClient,
) -> None:
    """
    Listen to messages from an XRPL Websocket client and handle them.

    Args:
        client (AsyncWebsocketClient): The XRPL Websocket client to listen for messages.
    """
    async for message in client:
        print(message)
        if message["status"] == "success":
            break
        if message["status"] == "error":
            return

    async for message in client:
        print(message)
        # Check if 'alternatives' key is present directly in the message
        if message["alternatives"]:
            source_amount = float(message["alternatives"][0]["source_amount"])
            dest_amount_value = float(message["destination_amount"]["value"])

            # Calculate the exchange rate
            exchange_rate = source_amount / dest_amount_value
            print(exchange_rate)

        else:
            # If 'alternatives' key is not directly in the message, it might be in the 'result' key
            # or the message structure might be different.
            # So, just printing the message for now.
            print(message)


async def exchange_rate_stream(
    source_address: str,
    destination_address: str,
    destination_amount: Amount,
    client: AsyncWebsocketClient,
    send_amount: Optional[Amount] = None,
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
    await client.send(
        PathFind(
            source_account=source_address,
            destination_account=destination_address,
            destination_amount=destination_amount.to_xrpl_amount(),
            send_max=send_amount.to_xrpl_amount() if send_amount else None,
            subcommand=PathFindSubcommand.CREATE,
        )
    )


async def connect_websockets() -> None:
    ws_client = get_xrpl_ws_client()
    async with ws_client as client:
        listener_task = asyncio.create_task(listener(client))
        await exchange_rate_stream(
            source_address="rL8uh4GEBX8Yn9yReKjmikzTBzQNLVYTzV",
            destination_address="rL8uh4GEBX8Yn9yReKjmikzTBzQNLVYTzV",
            destination_amount=Amount(symbol="USD", issuer="rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq", value="1"),
            # send_amount=Amount(
            #     symbol="534F4C4F00000000000000000000000000000000",
            #     issuer="rsoLo2S1kiGeCcn6hCUXVrCpGMWLrRrLZz",
            #     value="5",
            # ),
            client=client,
        )
        await listener_task
    # # 각 조합에 대해 exchange_rate_stream 함수를 호출
    # tasks = [
    #     exchange_rate_stream(
    #         source_address="rL8uh4GEBX8Yn9yReKjmikzTBzQNLVYTzV",
    #         destination_address="rL8uh4GEBX8Yn9yReKjmikzTBzQNLVYTzV",
    #         destination_amount=combo["destination_amount"],
    #         send_amount=combo["send_amount"],
    #         client=get_xrpl_ws_client(),
    #     )
    #     for combo in amount_combinations
    # ]

    # # 모든 웹소켓 연결을 동시에 시작
    # asyncio.run(asyncio.gather(*tasks))


if __name__ == "__main__":
    asyncio.run(connect_websockets())
