import logging
from typing import Callable, Iterable

from src.models.enums import Insurance
from src.models.user import (
    UserInput,
    UserOutput,
    UserScore,
    UserScoreEligibility,
)

logger = logging.getLogger(__name__)


def _calculate_base_score(risk_questions: Iterable) -> UserScore:
    logger.info("Calculating base score")
    base_score = sum(risk_questions)

    return UserScore(
        disability=UserScoreEligibility(
            score=base_score,
        ),
        auto=UserScoreEligibility(
            score=base_score,
        ),
        home=UserScoreEligibility(
            score=base_score,
        ),
        life=UserScoreEligibility(
            score=base_score,
        ),
    )


def calculate_insurance(
    user_input: UserInput,
    rules: tuple[Callable[[UserInput, UserScore], UserScore]],
) -> UserOutput:
    user_score = _calculate_base_score(user_input.risk_questions)
    logger.info("Starting running the rules")
    for rule in rules:
        user_score = rule(user_input=user_input, user_score=user_score)
    logger.info("All rules passed")

    return UserOutput(
        auto=_calculate_insurance_score(user_score.auto),
        home=_calculate_insurance_score(user_score.home),
        disability=_calculate_insurance_score(user_score.disability),
        life=_calculate_insurance_score(user_score.life),
    )


def _calculate_insurance_score(
    score_value: UserScoreEligibility,
) -> Insurance:
    if not score_value.eligible:
        return Insurance.INELIGIBLE
    if score_value.score <= 0:
        return Insurance.ECONOMIC
    if score_value.score >= 3:
        return Insurance.RESPONSIBLE
    else:
        return Insurance.REGULAR
