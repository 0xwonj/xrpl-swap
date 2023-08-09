from xrpl.models.transactions import Transaction
from xrpl.wallet import Wallet
from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.asyncio.transaction import (
    autofill,
    sign,
    submit_and_wait,
    XRPLReliableSubmissionException,
)

from app.models.types import Result


async def submit_transaction(
    transaction: Transaction,
    client: AsyncJsonRpcClient,
    wallet: Wallet,
) -> Result:
    """
    Submits a transaction to XRPL, waits for a response, and returns the result.

    Args:
        transaction (Transaction): The transaction object to be submitted to the network.
        client (AsyncJsonRpcClient): The JSON RPC client used to communicate with the network.
        wallet (Wallet): The wallet containing the keys used to sign the transaction.

    Raises:
        XRPLReliableSubmissionException: If the transaction is not successful, this exception is raised with the result of the transaction.

    Returns:
        Result: The result object containing the transaction's outcome details.
    """

    # Autofill transaction
    filled_tx = await autofill(transaction=transaction, client=client, signers_count=1)

    # Sign transaction
    signed_tx = sign(transaction=filled_tx, wallet=wallet, multisign=False)

    # Validate transaction
    signed_tx.validate()

    # Send transaction and get response
    response = await submit_and_wait(
        transaction=signed_tx, client=client, wallet=wallet
    )

    # Raise exception if transaction failed
    if not response.is_successful():
        raise XRPLReliableSubmissionException(response.result)

    # Return result
    return Result(data=response.result)
