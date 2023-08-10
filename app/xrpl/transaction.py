from fastapi.responses import JSONResponse
from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.asyncio.transaction import autofill, sign, submit_and_wait
from xrpl.models.transactions import Transaction
from xrpl.wallet import Wallet

from app.xrpl.client import create_json_response


async def submit_transaction(
    transaction: Transaction,
    client: AsyncJsonRpcClient,
    wallet: Wallet,
) -> JSONResponse:
    """
    Submits a transaction to XRPL, waits for a response, and then returns the result.

    Args:
        transaction (Transaction): Transaction object to be submitted to XRP Ledger.
        client (AsyncJsonRpcClient): Async JSON RPC client for XRP Ledger.
        wallet (Wallet): The wallet containing the keys used for signing the transaction.

    Returns:
        JSONResponse: A JSON response containing details about the outcome of the transaction.
                   Returns with a status code of 200 on success and 400 on failure.
    """
    # Autofill transaction
    filled_tx = await autofill(transaction=transaction, client=client, signers_count=1)

    # Sign transaction
    signed_tx = sign(transaction=filled_tx, wallet=wallet, multisign=False)

    # Validate transaction
    signed_tx.validate()

    # Send transaction and get response
    response = await submit_and_wait(transaction=signed_tx, client=client, wallet=wallet)

    # Return response
    return create_json_response(response)
