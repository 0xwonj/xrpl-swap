from redis.asyncio import Redis
from xrpledger.models import Token


async def get_quality(token_pair: tuple[Token, Token], amount: float, redis: Redis) -> float:
    """
    Fetches the quality for a given token pair and amount from Redis.

    Args:
        token_pair (tuple[Token, Token]): A tuple representing the token pair.
        amount (float): The amount for which the quality is needed.
        redis (Redis): Redis client to fetch data.

    Returns:
        float: The quality of the token pair for the given amount. Returns -1.0 if not found.
    """
    token_key = f"{token_pair[0]}/{token_pair[1]}"
    result: list[float] = await redis.zrangebyscore(token_key, amount, "+inf", start=0, num=1)
    
    return float(result[0]) if result else -1.0
