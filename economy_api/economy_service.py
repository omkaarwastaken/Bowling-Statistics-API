
from utils.math_utils import clamp_score


def economy_label(score: float):
    """
    Convert numeric score into
    qualitative interpretation.
    """

    if score >= 80:
        return "Elite Suppression"

    if score >= 65:
        return "Above Average Control"

    if score >= 50:
        return "Competitive"

    if score >= 35:
        return "Below Average"

    return "Expensive Spell"


def economy_interpretation(score: float):
    """
    Generate analytical interpretation.
    """

    if score >= 80:
        return (
            "The bowler is dramatically outperforming "
            "the bowling environment."
        )

    if score >= 65:
        return (
            "The bowler is outperforming the environment "
            "with strong run control."
        )

    if score >= 50:
        return (
            "The bowler is slightly above the "
            "population baseline."
        )

    if score >= 35:
        return (
            "The bowler is slightly below the "
            "expected bowling standard."
        )

    return (
        "The bowler is significantly more expensive "
        "than the surrounding bowling population."
    )


def calculate_economy_metrics(data):
    """
    Economy Deviation Formula

    Step 1:
    Calculate bowler economy.

    bowler_economy = runs_conceded / overs_bowled

    Step 2:
    Compare against population mean using
    a z-score style comparison.

    z = (
        population_mean - bowler_economy
    ) / population_std_dev

    Step 3:
    Convert into a 0–100 score.
    """

    # Bowler economy
    bowler_economy = (
        data.runs_conceded /
        data.overs_bowled
    )

    # Relative comparison score
    z_score = (
        data.population_mean_economy
        - bowler_economy
    ) / data.population_std_dev

    # Convert to scaled score
    score = 50 + (z_score * 15)

    # Restrict between 0 and 100
    score = clamp_score(score)

    return {
        "runs_conceded": data.runs_conceded,
        "overs_bowled": data.overs_bowled,

        "bowler_economy": round(
            bowler_economy,
            2
        ),

        "population_mean":
        data.population_mean_economy,

        "population_spread":
        data.population_std_dev,

        "economy_deviation_score":
        round(score, 2),

        "label":
        economy_label(score),

        "interpretation":
        economy_interpretation(score)
    }

