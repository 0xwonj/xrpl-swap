from typing import Annotated

from pydantic import BaseModel, Field


class AccountData(BaseModel):
    """
    A model representing the account data from the get_account_info endpoint.
    """

    Account: str
    Balance: Annotated[int, Field(description="The XRP balance in drops. 10^6 drops = 1 XRP")]
    Flags: int
    LedgerEntryType: str
    OwnerCount: int
    PreviousTxnID: str
    PreviousTxnLgrSeq: int
    Sequence: int
    index: str


class AccountFlags(BaseModel):
    """
    A model representing the account flags from the get_account_info endpoint.
    """

    defaultRipple: bool
    depositAuth: bool
    disableMasterKey: bool
    disallowIncomingCheck: bool
    disallowIncomingNFTokenOffer: bool
    disallowIncomingPayChan: bool
    disallowIncomingTrustline: bool
    disallowIncomingXRP: bool
    globalFreeze: bool
    noFreeze: bool
    passwordSpent: bool
    requireAuthorization: bool
    requireDestinationTag: bool


class AccountInfoResponse(BaseModel):
    """
    A model representing the response from the get_account_info endpoint.
    """

    account_data: AccountData
    account_flags: AccountFlags
    ledger_current_index: int
    validated: bool

    class Config:
        """
        Pydantic model configuration.
        """

        json_schema_extra = {
            "example": {
                "account_data": {
                    "Account": "rnwjHhgiNQSYfJndh1AiRBmcRKmPu2qzGs",
                    "Balance": "10000000000",
                    "Flags": 0,
                    "LedgerEntryType": "AccountRoot",
                    "OwnerCount": 0,
                    "PreviousTxnID": "D2E895DDF5DCC40DA3B9140F75607EDBC5E98DC8CEE3DAC746053F381B557B35",
                    "PreviousTxnLgrSeq": 40163988,
                    "Sequence": 40163951,
                    "index": "99B28FBDE1B215D535E46A927DA109B66DA61148DE8CB52E7EE65DF469CBA9E5",
                },
                "account_flags": {
                    "defaultRipple": False,
                    "depositAuth": False,
                    "disableMasterKey": False,
                    "disallowIncomingCheck": False,
                    "disallowIncomingNFTokenOffer": False,
                    "disallowIncomingPayChan": False,
                    "disallowIncomingTrustline": False,
                    "disallowIncomingXRP": False,
                    "globalFreeze": False,
                    "noFreeze": False,
                    "passwordSpent": False,
                    "requireAuthorization": False,
                    "requireDestinationTag": False,
                },
                "ledger_current_index": 40241037,
                "validated": False,
            }
        }
