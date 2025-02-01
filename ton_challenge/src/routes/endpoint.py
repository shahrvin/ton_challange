from fastapi import APIRouter
from address_generator import ton_wallet_sdk

router = APIRouter()

@router.get("/generate-ton-address")
def generate_address():
    """
    Endpoint to generate a TON wallet address.
    """
    return ton_wallet_sdk()