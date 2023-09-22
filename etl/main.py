import asyncio
from itertools import combinations

from database.redis import get_redis
from etl.offer import calculate_quality, extract_offers, quality_to_redis
from xrpledger.client import get_xrpl_rpc_client
from xrpledger.data.tokens import tokens
from xrpledger.models import Token


async def etl_offers(token_pair: tuple[Token, Token]) -> None:
    """
    Extract, transform, and load offer data into Redis

    Args:
        token_pair (tuple[Token, Token]): token pair
    """
    offers = await extract_offers(
        taker_gets=token_pair[0],
        taker_pays=token_pair[1],
        client=get_xrpl_rpc_client(),
    )
    quality = calculate_quality(offers, token_pair)
    await quality_to_redis(quality, redis=get_redis())


async def process_token_pair(token_pair: tuple[Token, Token]) -> None:
    """
    Continuously process a token pair every 3 seconds
    """
    while True:
        await etl_offers(token_pair)
        await asyncio.sleep(3)


async def main() -> None:
    """
    Main function
    """
    token_pairs = list(combinations(tokens.values(), 2))

    tasks = [process_token_pair(pair) for pair in token_pairs]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
