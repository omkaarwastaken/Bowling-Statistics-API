
from pydantic import BaseModel, Field


class EconomyRequest(BaseModel):
    """
    Request payload for
    Economy Deviation API.
    """

    runs_conceded: float = Field(
        ...,
        ge=0,
        description="Total runs conceded by the bowler"
    )

    overs_bowled: float = Field(
        ...,
        gt=0,
        description="Total overs bowled"
    )

    population_mean_economy: float = Field(
        ...,
        ge=0,
        description="Average economy of comparison population"
    )

    population_std_dev: float = Field(
        ...,
        gt=0,
        description="Standard deviation of population economy"
    )


class EconomyResponse(BaseModel):
    """
    Response model for
    Economy Deviation API.
    """

    runs_conceded: float
    overs_bowled: float

    bowler_economy: float

    population_mean: float
    population_spread: float

    economy_deviation_score: float

    label: str
    interpretation: str

