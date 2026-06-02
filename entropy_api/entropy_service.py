
import math

from utils.math_utils import (
    normalize_distribution,
    shannon_entropy,
    normalize_entropy,
    clamp_score
)


def entropy_label(control_score: float):
    """
    Convert control score into volatility class.
    """

    if control_score >= 8:
        return "Elite Control"

    if control_score >= 6:
        return "Structured Spell"

    if control_score >= 4:
        return "Chaotic Spell"

    return "Extreme Volatility"


def entropy_interpretation(control_score: float):
    """
    Human-readable tactical interpretation.
    """

    if control_score >= 8:
        return "The bowler is maintaining strong control over outcomes."

    if control_score >= 6:
        return "The spell shows reasonable discipline and structure."

    if control_score >= 4:
        return "The bowling is inconsistent with scattered outcomes."

    return "The bowler is highly unpredictable and erratic."


def calculate_entropy_metrics(data):
    """
    Control Entropy Model

    Step 1:
    Convert raw shares into probabilities.

    Step 2:
    Compute Shannon entropy.

    Step 3:
    Normalize entropy.

    Step 4:
    Invert into control score.
    """

    # Raw outcome values
    raw_values = [
        data.dot_ball_share,
        data.single_share,
        data.boundary_share
    ]

    # Normalize distribution
    probabilities = normalize_distribution(raw_values)

    # Compute entropy
    entropy = shannon_entropy(probabilities)

    # Maximum entropy for 3 outcomes
    max_entropy = math.log2(len(probabilities))

    # Normalize entropy
    normalized = normalize_entropy(entropy, max_entropy)

    # Convert to control score
    control_score = 10 * (1 - normalized)

    # Clamp score
    control_score = clamp_score(control_score)

    return {
        "outcome_distribution": {
            "dot_ball_probability": round(probabilities[0], 3),
            "single_probability": round(probabilities[1], 3),
            "boundary_probability": round(probabilities[2], 3),
        },

        "entropy": round(entropy, 3),
        "normalized_entropy": round(normalized, 3),

        "control_score": round(control_score, 2),

        "volatility_tag": entropy_label(control_score),

        "tactical_read": entropy_interpretation(control_score)
    }

