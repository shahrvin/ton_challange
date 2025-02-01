from pydantic import BaseModel

class TonAddressResponse(BaseModel):
    wallet_address: str
    private_key: str