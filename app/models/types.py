from typing import Dict, Any

from pydantic import BaseModel, Field, validator

from xrpl.core.addresscodec import is_valid_classic_address, is_valid_xaddress


class Address(BaseModel):
    value: str = Field(..., min_length=25, max_length=58)

    # pylint: disable=no-self-argument
    @validator("value")
    def validate_address(cls, value: str) -> str:
        if not is_valid_classic_address(value) and not is_valid_xaddress(value):
            raise ValueError("Invalid address")
        return value


class Result(BaseModel):
    data: Dict[str, Any]


class TokenAmount(BaseModel):
    currency: str
    issuer: str
    value: str | int | float
