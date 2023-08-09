from typing import Any, Dict

from pydantic import BaseModel, Field, validator
from xrpl.core.addresscodec import is_valid_classic_address, is_valid_xaddress


class Address(BaseModel):
    """
    A model representing an XRPL address.

    Raises:
        ValueError: If the provided address is not in a valid format.
    """

    value: str = Field(
        ...,
        min_length=25,
        max_length=58,
        description="An XRPL address, either in classic or X-address format",
    )

    # pylint: disable=no-self-argument
    @validator("value")
    def validate_address(cls, value: str) -> str:
        """
        Validates whether the provided value is a valid XRPL address.

        Args:
            value (str): The XRPL address string to validate.

        Returns:
            str: The validated XRPL address.

        Raises:
            ValueError: If the provided address is neither in classic nor X-address format.
        """
        if not is_valid_classic_address(value) and not is_valid_xaddress(value):
            raise ValueError("Invalid address")
        return value


class Result(BaseModel):
    """
    A model representing the result of a transaction or operation.
    """

    data: Dict[str, Any] = Field(..., description="A dictionary of the result")


class TokenAmount(BaseModel):
    """
    A model representing the amount details of a token.
    """

    currency: str = Field(..., description="The currency code or symbol of the token")
    issuer: str = Field(..., description="The issuer's XRPL address")
    value: str | int | float = Field(..., description="The amount value of the token")
