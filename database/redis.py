import redis.asyncio as redis

from common.config import settings


def create_redis_pool() -> redis.ConnectionPool:
    """
    Create a new Redis connection pool.

    Returns:
        redis.ConnectionPool: A connection pool object of a Redis server.
    """
    return redis.ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        encoding="utf-8",
        decode_responses=True,
        protocol=3,
    )


redis_pool = create_redis_pool()


def get_redis() -> redis.Redis:
    """
    Retrieve a Redis connection from the connection pool.

    Returns:
        redis.Redis: A Redis connection object, which can be used to execute Redis commands.
    """
    return redis.Redis(connection_pool=redis_pool)
