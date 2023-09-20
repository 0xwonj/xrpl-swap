from redis.asyncio import Redis


async def quality_to_redis(quality: dict[str, dict[float, float]], redis: Redis) -> None:
    """
    Saves the quality data of token pairs to a Redis store.

    Args:
        quality (dict[str, dict[float, float]]): A mapping of token pairs to their respective quality data.
        redis (Redis): Redis client to handle data storage operations.

    """
    for token_key, token_quality in quality.items():
        swapped_quality = {value: key for key, value in token_quality.items()}
        await redis.delete(token_key)
        await redis.zadd(token_key, swapped_quality)
