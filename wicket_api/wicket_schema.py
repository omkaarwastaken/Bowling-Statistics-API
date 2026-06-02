from pydantic import BaseModel, Field


class WicketRequest(BaseModel):

    total_balls: int = Field(
        ...,
        gt=0
    )

    total_wickets: int = Field(
        ...,
        ge=0
    )

    phase: str = Field(
        ...,
        description="powerplay, middle, death"
    )

    opportunity_balls: int = Field(
        ...,
        gt=0
    )

    avg_xwicket: float = Field(
        ...,
        ge=0,
        le=1
    )

    avg_risk: float = Field(
        ...,
        ge=0,
        le=1
    )

    avg_pressure: float = Field(
        ...,
        ge=0,
        le=1
    )

    avg_control: float = Field(
        ...,
        ge=0,
        le=1
    )


class WicketResponse(BaseModel):

    total_balls: int
    total_wickets: int

    phase: str
    phase_multiplier: float

    avg_xwicket: float
    avg_risk: float
    avg_pressure: float
    avg_control: float

    wicket_rate: float

    expected_wickets: float

    wicket_likelihood_score: float

    label: str
    interpretation: str