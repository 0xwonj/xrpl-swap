from typing import Annotated

import redis.asyncio as redis
from fastapi import Depends, Path
from xrpl.asyncio.clients import AsyncJsonRpcClient

from common.config import settings
from common.constants import XRPL_ADDRESS_REGEX
from database.redis import get_redis
from xrpledger.client import get_xrpl_client

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
