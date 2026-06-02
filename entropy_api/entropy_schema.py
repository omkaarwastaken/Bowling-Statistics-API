
from pydantic import BaseModel, Field


class EntropyRequest(BaseModel):
    """
    Request model for Control Entropy API.
    Represents outcome distribution in a bowling spell.
    """

    dot_ball_share: float = Field(
        ...,
        ge=0,
        description="Percentage of dot balls"
    )

    single_share: float = Field(
        ...,
        ge=0,
        description="Percentage of singles conceded"
    )

    boundary_share: float = Field(
        ...,
        ge=0,
        description="Percentage of boundaries conceded"
    )


class EntropyResponse(BaseModel):
    """
    Response model for Control Entropy API.
    """

    outcome_distribution: dict

    entropy: float
    normalized_entropy: float

    control_score: float

    volatility_tag: str
    tactical_read: str

