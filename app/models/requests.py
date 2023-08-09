from pydantic import BaseModel

from app.models.types import TokenAmount


class TokenSwapRequest(BaseModel):
    """
    A model representing the request for a token swap.

    Attributes:
        source (TokenAmount): The source token amount details for the swap.
        dest (TokenAmount): The destination token amount details for the swap.
        secret (str): The secret key of the user's XRPL account.
        public (str): The public key of the user's XRPL account.
    """

    source: TokenAmount
    dest: TokenAmount
    secret: str
    public: str
