from typing import Optional

from pydantic import BaseModel, Field, validator

from app.models.annotations import XrplAddress
from xrpledger.data.tokens import tokens
from xrpledger.models import Amount, Token


class PaymentRequest(BaseModel):
    """
    A model representing the request for a token swap.
    """

    account: XrplAddress = Field(..., description="The XRPL address of the account initiating the swap")

    destination: XrplAddress = Field(..., description="The XRPL address of the account receiving the swap")

    amount: Amount = Field(..., description="The destination token amount details for the swap")

    send_max: Optional[Amount] = Field(..., description="The source token amount details for the swap")

    deliver_min: Optional[Amount] = Field(..., description="The minimum amount to deliver")

    secret: str
    public: str


class OfferQualityRequest(BaseModel):
    """
    A model representing the request for a token swap.
    """

    token_from: Token = Field(..., description="The source token for the swap", example=tokens["XRP"])

    token_to: Token = Field(
        ..., description="The destination token for the swap", example=tokens["USD.Gatehub"]
    )

    from_amount: float = Field(..., ge=0, description="The source token amount for the swap")

    @validator("token_to", pre=True, always=True)
    def validate_token_pair(cls, token_to: Token, values: dict) -> Token:
        """
        Validate token pair
        """
        token_from = values.get("token_from")
        if token_from == token_to:
            raise ValueError("token_from and token_to should be different")
        return token_to


class OfferCreateRequest(BaseModel):
    """
    A model representing the request for a token offer create.
    """

    account: XrplAddress = Field(..., description="The XRPL address of the account initiating the offer")

    taker_gets: Amount = Field(..., description="The token amount that the taker gets")

    taker_pays: Amount = Field(..., description="The token amount that the taker pays")

    secret: str  # this is temporary
    public: str  # this is temporary


class OfferCancelRequest(BaseModel):
    """
    A model representing the request for a token offer create.
    """

    account: XrplAddress = Field(..., description="The XRPL address of the account initiating the offer")

    offer_sequence: int

    secret: str  # this is temporary
    public: str  # this is temporary
