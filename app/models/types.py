from typing import Any, Dict

from pydantic import BaseModel, Field, validator
from xrpl.core.addresscodec import is_valid_classic_address, is_valid_xaddress


class Address(BaseModel):
    """
    A model representing an XRPL address.

    Attributes:
        value (str): The XRPL address string, either in classic or X-address format.

    Raises:
        ValueError: If the provided address is not in a valid format.
    """

    value: str = Field(..., min_length=25, max_length=58)

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

    Attributes:
        data (Dict[str, Any]): A dictionary containing the data related to the result.
    """

    data: Dict[str, Any]


class TokenAmount(BaseModel):
    """
    A model representing the amount details of a token.

    Attributes:
        currency (str): The currency code or symbol of the token.
        issuer (str): The issuer's XRPL address.
        value (str|int|float): The amount value of the token.
    """

    currency: str
    issuer: str
    value: str | int | float
