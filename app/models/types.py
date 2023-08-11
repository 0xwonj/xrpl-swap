from typing import Optional

from pydantic import BaseModel, validator


class Wallet(BaseModel):
    """
    A model representing a XRP Ledger wallet.
    """

    address: str
    public_key: str
    private_key: str


class Amount(BaseModel):
    """
    A model representing the amount details of a token or XRP.
    """

    symbol: str
    issuer: Optional[str]
    value: str | int | float

    @validator("issuer", pre=True, always=True)
    def set_issuer(cls, val, values) -> Optional[str]:
        """
        Validate and set the issuer field based on the provided symbol.

        For XRP, the issuer is optional and can be set to None. For other symbols,
        an issuer must be provided.

        Args:
            val (Optional[str]): The issuer value provided to the Amount model.
            values (dict): A dictionary of field values in the Amount model.

        Raises:
            ValueError: If the symbol is not "XRP" and no issuer value is provided.

        Returns:
            Optional[str]: The validated issuer value or None for XRP symbol.
        """
        # If the symbol is "XRP", the issuer is optional and can be None.
        if values.get("symbol") == "XRP":
            return val
        # For other symbols, the issuer must be provided.
        if not val:
            raise ValueError("Issuer is required for non-XRP symbols.")
        return val
