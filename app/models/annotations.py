from typing import Annotated

import redis.asyncio as redis
from fastapi import Depends, Path
from xrpl.asyncio.clients import AsyncJsonRpcClient

from app.common.config import settings
from app.common.constants import XRPL_ADDRESS_REGEX
from app.database.redis import get_redis
from app.xrpl.client import get_xrpl_client

XrplAddress = Annotated[
    str,
    Path(
        ...,
        description="The XRPL address of the user.",
        example=settings.wallet.address,
        pattern=XRPL_ADDRESS_REGEX,
    ),
]

XrplClient = Annotated[AsyncJsonRpcClient, Depends(get_xrpl_client)]

Redis = Annotated[redis.Redis, Depends(get_redis)]
