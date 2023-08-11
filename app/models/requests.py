from typing import Annotated

from pydantic import BaseModel, Field

from app.models.types import Amount


class TokenSwapRequest(BaseModel):
    """
    A model representing the request for a token swap.
    """

    source: Annotated[Amount, Field(..., description="The source token amount details for the swap")]
    dest: Annotated[Amount, Field(..., description="The destination token amount details for the swap")]
    secret: str
    public: str
