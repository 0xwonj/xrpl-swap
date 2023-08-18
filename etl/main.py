import asyncio

from etl.xrpl.exchange_rate import exchange_rate_stream
from etl.xrpl.exchange_rate import listener as exchange_rate_listener
from xrpledger.client import get_xrpl_ws_client
from xrpledger.models import Amount


async def connect_xrpl() -> None:
    """
    Establish a connection to the XRPL websockets and initiate streams.
    """
    ws_client = get_xrpl_ws_client()

    async with ws_client as client:
        listener_task = asyncio.create_task(exchange_rate_listener(client))

        await exchange_rate_stream(
            source_address="rL8uh4GEBX8Yn9yReKjmikzTBzQNLVYTzV",
            destination_address="rL8uh4GEBX8Yn9yReKjmikzTBzQNLVYTzV",
            destination_amount=Amount(symbol="USD", issuer="rhub8VRN55s94qWKDv6jmDy1pUykJzF3wq", value="1"),
            client=client,
        )

        await listener_task


async def main() -> None:
    """
    Run the main application.
    """
    await connect_xrpl()


if __name__ == "__main__":
    asyncio.run(main())
