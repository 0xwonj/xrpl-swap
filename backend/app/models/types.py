from typing import Dict, Any

from pydantic import BaseModel, Field


class Address(BaseModel):
    value: str = Field(..., min_length=34, max_length=34)


class Result(BaseModel):
    data: Dict[str, Any]
