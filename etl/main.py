import asyncio

from database.redis import get_redis
from etl.orderbook import calculate_quality, extract_orderbook, quality_to_redis
from xrpledger.client import get_xrpl_client
from xrpledger.data.tokens import tokens
from xrpledger.models import Token


async def etl_orderbook(token_pair: tuple[Token, Token]):
    """
    Extract, transform, and load orderbook data into Redis

    Args:
        token_pair (tuple[Token, Token]): token pair
    """
    await get_redis().flushall()
    offers = await extract_orderbook(
        taker_gets=token_pair[0],
        taker_pays=token_pair[1],
        client=get_xrpl_client(),
    )
    quality = calculate_quality(offers, token_pair)
    await quality_to_redis(quality, redis=get_redis())


async def main():
    """
    Main function
    """
    await etl_orderbook((tokens["USD.Gatehub"], tokens["XRP"]))


if __name__ == "__main__":
    asyncio.run(main())
