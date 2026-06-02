from utils.math_utils import clamp_score


def wicket_label(score: float):

    if score >= 80:
        return "Extreme Threat"

    if score >= 60:
        return "High Threat"

    if score >= 40:
        return "Developing Threat"

    if score >= 20:
        return "Occasional Threat"

    return "Low Threat"


def wicket_interpretation(score: float):

    if score >= 60:
        return "The bowler consistently creates wicket pressure."

    if score >= 40:
        return "The bowler shows moderate wicket-taking ability."

    if score >= 20:
        return "The bowler creates occasional wicket chances."

    return "The bowler currently poses low wicket threat."


def get_phase_multiplier(
    phase: str
) -> float:

    phase = phase.lower()

    phase_map = {
        "powerplay": 1.10,
        "middle": 0.95,
        "death": 1.20
    }

    return phase_map.get(
        phase,
        1.00
    )


def calculate_wicket_metrics(data):

    wicket_rate = (
        data.total_wickets /
        data.total_balls
    )

    phase_multiplier = get_phase_multiplier(
        data.phase
    )

    avg_threat = (
        data.avg_xwicket * 0.50 +
        data.avg_risk * 0.20 +
        data.avg_pressure * 0.15 +
        (1 - data.avg_control) * 0.15
    )

    adjusted_threat = (
        avg_threat *
        phase_multiplier
    )

    expected_wickets = (
        adjusted_threat *
        data.opportunity_balls
    )

    score = (
        adjusted_threat +
        wicket_rate * 0.30
    ) * 100

    score = clamp_score(score)

    return {
        "total_balls": data.total_balls,
        "total_wickets": data.total_wickets,

        "phase": data.phase,
        "phase_multiplier": round(
            phase_multiplier,
            2
        ),

        "avg_xwicket": round(
            data.avg_xwicket,
            4
        ),

        "avg_risk": round(
            data.avg_risk,
            4
        ),

        "avg_pressure": round(
            data.avg_pressure,
            4
        ),

        "avg_control": round(
            data.avg_control,
            4
        ),

        "wicket_rate": round(
            wicket_rate,
            4
        ),

        "expected_wickets": round(
            expected_wickets,
            2
        ),

        "wicket_likelihood_score": round(
            score,
            2
        ),

        "label": wicket_label(score),

        "interpretation": wicket_interpretation(score)
    }