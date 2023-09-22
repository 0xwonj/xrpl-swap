from xrpledger.models import Token


def calculate_quality(
    offers: list[dict[str, any]], token_pair: tuple[Token, Token]
) -> dict[str, dict[float, float]]:
    """
    Calculates the quality of offers for a given token pair.

    Args:
        offers (list[dict[str, any]]): A list of offer data for the token pair.
        token_pair (tuple[Token, Token]): A tuple representing the token pair.

    Returns:
        dict[str, dict[float, float]]: A mapping of token pairs to their respective calculated quality data.
    """
    token_key = f"{token_pair[0]}/{token_pair[1]}"
    token_key_inverse = f"{token_pair[1]}/{token_pair[0]}"
    quality = {token_key: {}, token_key_inverse: {}}

    total_get = 0
    total_pay = 0

    for offer in offers:
        key = "taker_gets_funded" if "taker_gets_funded" in offer else "TakerGets"
        get_amount = float(offer[key]["value"] if isinstance(offer[key], dict) else offer[key])

        key = "taker_pays_funded" if "taker_pays_funded" in offer else "TakerPays"
        pay_amount = float(offer[key]["value"] if isinstance(offer[key], dict) else offer[key])

        total_get += get_amount
        total_pay += pay_amount

        try:
            quality[token_key][total_get] = total_pay / total_get
        except ZeroDivisionError:
            quality[token_key][total_get] = 0

        try:
            quality[token_key_inverse][total_pay] = total_get / total_pay
        except ZeroDivisionError:
            quality[token_key_inverse][total_pay] = 0

    return quality
