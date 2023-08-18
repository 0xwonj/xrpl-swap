from typing import Any

from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.asyncio.transaction import autofill, sign, submit_and_wait
from xrpl.models.transactions import Transaction
from xrpl.wallet import Wallet


async def submit_transaction(
    transaction: Transaction,
    wallet: Wallet,
    client: AsyncJsonRpcClient,
) -> dict[str, Any]:
    """
    Submits a transaction to XRPL, waits for a response, and then returns the result.

    Args:
        transaction (Transaction): Transaction object to be submitted to XRP Ledger.
        client (AsyncJsonRpcClient): Async JSON RPC client for XRP Ledger.
        wallet (Wallet): The wallet containing the keys used for signing the transaction.

    Returns:
        dict[str, Any]: The result of the transaction.
    """
    # Autofill transaction
    filled_tx = await autofill(transaction=transaction, client=client, signers_count=1)

    # Sign transaction
    signed_tx = sign(transaction=filled_tx, wallet=wallet, multisign=False)

    # Validate transaction
    signed_tx.validate()

    # Send transaction and get response
    response = await submit_and_wait(transaction=signed_tx, client=client, wallet=wallet)

    # Return result as dictionary
    return response.result
