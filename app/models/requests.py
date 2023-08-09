from pydantic import BaseModel
from app.models.types import TokenAmount


class TokenSwapRequest(BaseModel):
    source: TokenAmount
    dest: TokenAmount
    secret: str
    public: str
