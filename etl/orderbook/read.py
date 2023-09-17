from redis.asyncio import Redis
from xrpledger.models import Token


async def get_quality(token_pair: tuple[Token, Token], amount: float, redis: Redis) -> float:
    """_summary_

    Args:
        token_pair (tuple[Token, Token]): _description_
        amount (float): _description_
        redis (Redis): _description_

    Returns:
        float: _description_
    """
    token_key = f"{token_pair[0]}/{token_pair[1]}"

    result = await redis.zrangebyscore(token_key, amount, "+inf", start=0, num=1)
    if result:
        return float(result[0])
    return -1.0
