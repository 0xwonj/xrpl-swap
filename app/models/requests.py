from pydantic import BaseModel, Field

from app.models.types import TokenAmount


class TokenSwapRequest(BaseModel):
    """
    A model representing the request for a token swap.
    """

    source: TokenAmount = Field(..., description="The source token amount details for the swap")
    dest: TokenAmount = Field(..., description="The destination token amount details for the swap")
    secret: str
    public: str
