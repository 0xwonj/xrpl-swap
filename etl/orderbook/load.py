from redis.asyncio import Redis


async def quality_to_redis(quality: dict[str, dict[float, float]], redis: Redis) -> None:
    """_summary_

    Args:
        quality (dict[str, dict[float, float]]): _description_
        redis (Redis): _description_
    """
    for token_key, token_quality in quality.items():
        swapped_quality = {value: key for key, value in token_quality.items()}
        await redis.delete(token_key)
        await redis.zadd(token_key, swapped_quality)
