
from fastapi import APIRouter

from entropy_api.entropy_schema import (
    EntropyRequest,
    EntropyResponse
)

from entropy_api.entropy_service import (
    calculate_entropy_metrics
)

# Router definition
router = APIRouter(
    prefix="/entropy",
    tags=["Control Entropy API"]
)


@router.post(
    "/analyze",
    response_model=EntropyResponse
)
async def analyze_entropy(
    data: EntropyRequest
):
    """
    Analyze bowling control using
    entropy of outcome distribution.
    """

    return calculate_entropy_metrics(data)

