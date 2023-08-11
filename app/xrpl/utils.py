from fastapi import HTTPException

from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.currencies import XRP

from app.models.types import Amount


def convert_to_amount(amount: Amount) -> str | IssuedCurrencyAmount:
    """
    Convert the given amount object to a specific currency format.

    If the amount symbol is "XRP", convert it to XRP format. For other tokens,
    an issuer is required and the function returns an IssuedCurrencyAmount.

    Args:
        amount (Amount): The amount object containing details like symbol, value, and issuer.

    Returns:
        str | IssuedCurrencyAmount: Returns XRP formatted amount or IssuedCurrencyAmount.

    Raises:
        HTTPException - 422: If issuer is missing for non-XRP tokens.
    """
    # If the symbol is XRP, convert to XRP format
    if amount.symbol == "XRP":
        return XRP().to_amount(amount.value)

    # Ensure that issuer is provided for tokens other than XRP
    if amount.issuer is None:
        raise HTTPException(status_code=422, detail="Issuer is required for non-XRP tokens.")

    # Return the amount in the format of IssuedCurrencyAmount
    return IssuedCurrencyAmount(currency=amount.symbol, issuer=amount.issuer, value=amount.value)
