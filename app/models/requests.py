from typing import Optional

from pydantic import BaseModel, Field

from app.models.annotations import XrplAddress
from app.models.types import Amount


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
