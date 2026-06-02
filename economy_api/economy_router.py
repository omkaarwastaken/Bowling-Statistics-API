
from fastapi import APIRouter

from economy_api.economy_schema import (
    EconomyRequest,
    EconomyResponse
)

from economy_api.economy_service import (
    calculate_economy_metrics
)

# Create API router
router = APIRouter(
    prefix="/economy",
    tags=["Economy Deviation API"]
)


@router.post(
    "/analyze",
    response_model=EconomyResponse
)
async def analyze_economy(
    data: EconomyRequest
):
    """
    Analyze bowling economy relative
    to the tournament or match environment.
    """

    return calculate_economy_metrics(data)

