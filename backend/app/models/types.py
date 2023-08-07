from typing import Dict, Any

from pydantic import BaseModel, Field, validator

from xrpl.core.addresscodec import is_valid_classic_address, is_valid_xaddress


class Address(BaseModel):
    value: str = Field(..., min_length=25, max_length=58)

    @validator("value")
    # pylint: disable=no-self-argument
    def validate_address(cls, value: str):
        if not is_valid_classic_address(value) and not is_valid_xaddress(value):
            raise ValueError("Invalid address")
        return value


class Result(BaseModel):
    data: Dict[str, Any]
