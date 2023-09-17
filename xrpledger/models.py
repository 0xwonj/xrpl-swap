from typing import Optional

from pydantic import BaseModel, validator
from xrpl.models.amounts import Amount as XrplAmount
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.currencies import XRP, IssuedCurrency


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
    issuer: Optional[str] = None
    value: str

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

    @validator("value")
    def validate_value(cls, val: str) -> str:
        """
        Validate that the provided value is a valid numerical string.

        Args:
            val (str): The value provided to the Amount model.

        Raises:
            ValueError: If the value is not a valid numerical string.

        Returns:
            str: The validated value string.
        """
        try:
            float(val)  # Try converting the value to a float
        except ValueError as exc:
            raise ValueError("Value must be a valid numerical string.") from exc
        return val

    def to_xrpl_amount(self) -> XrplAmount:
        """
        Convert the Amount model to an XrplAmount model.

        Returns:
            XrplAmount: An instance of XrplAmount representing the amount details of a token or XRP.
        """
        if self.symbol == "XRP":
            return self.value
        if issuer := self.issuer:
            return IssuedCurrencyAmount(
                currency=self.symbol,
                issuer=issuer,
                value=self.value,
            )
        raise ValueError("Issuer is required for non-XRP symbols.")


class Token(BaseModel):
    """
    A model representing a token on the XRP Ledger.
    """

    currency: str
    issuer: str

    def to_xrpl_currency(self) -> IssuedCurrency | XRP:
        """
        Convert the Token model to an IssuedCurrency or XRP model.

        Returns:
            IssuedCurrency | XRP: Token instances of xrpl
        """
        if self.currency == "XRP" and self.issuer == "":
            return XRP()
        return IssuedCurrency(
            currency=self.currency,
            issuer=self.issuer,
        )

    def __str__(self) -> str:
        return f"{self.currency}.{self.issuer}"
