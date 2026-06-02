
from fastapi import APIRouter

from wicket_api.wicket_schema import (
    WicketRequest,
    WicketResponse
)

from wicket_api.wicket_service import (
    calculate_wicket_metrics
)

# Create router
router = APIRouter(
    prefix="/wicket",
    tags=["Wicket Probability API"]
)


@router.post(
    "/analyze",
    response_model=WicketResponse
)
async def analyze_wicket(
    data: WicketRequest
):
    """
    Analyze wicket-taking probability
    and threat level.
    """

    return calculate_wicket_metrics(data)

