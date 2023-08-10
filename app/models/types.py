from pydantic import BaseModel, Field


class Wallet(BaseModel):
    """
    A model representing a XRP Ledger wallet.
    """

    address: str
    public_key: str
    private_key: str


class TokenAmount(BaseModel):
    """
    A model representing the amount details of a token.
    """

    currency: str = Field(..., description="The currency code or symbol of the token")
    issuer: str = Field(..., description="The issuer's XRPL address")
    value: str | int | float = Field(..., description="The amount value of the token")
