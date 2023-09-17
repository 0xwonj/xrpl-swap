from xrpledger.models import Token


def calculate_quality(
    offers: list[dict[str, any]], token_pair: tuple[Token, Token]
) -> dict[str, dict[float, float]]:
    """_summary_

    Args:
        offers (list[dict[str, any]]): _description_
        token_pair (tuple[Token, Token]): _description_

    Returns:
        dict[str, dict[float, float]]: _description_
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

        quality[token_key][total_pay] = total_get / total_pay
        quality[token_key_inverse][total_get] = total_pay / total_get

    return quality
