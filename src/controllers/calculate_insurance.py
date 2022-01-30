from typing import Callable
from src.controllers import rules
from src.controllers.rules import (
    rule_1,
    rule_2,
    rule_3,
    rule_4,
    rule_5,
    rule_6,
    rule_7,
    rule_8,
)
from src.models.models import (
    Insurance,
    OutputScore,
    OutputScoreEligibility,
    UserInput,
    UserOutput,
)


def calculate_base_score(risk_questions):
    return sum(risk_questions)


def validation(user_input: UserInput, rules: tuple(Callable)):
    base_score = calculate_base_score(user_input.risk_questions)
    output_score = OutputScore(
        disability=OutputScoreEligibility(
            score=base_score,
        ),
        auto=OutputScoreEligibility(
            score=base_score,
        ),
        home=OutputScoreEligibility(
            score=base_score,
        ),
        life=OutputScoreEligibility(
            score=base_score,
        ),
    )
    rules = (
        rule_1,
        rule_2,
        rule_3,
        rule_4,
        rule_5,
        rule_6,
        rule_7,
        rule_8,
    )
    for rule in rules:
        output_score = rule(user_input, output_score)

    return UserOutput(
        auto=calculate_insurance(output_score.auto),
        home=calculate_insurance(output_score.home),
        disability=calculate_insurance(output_score.disability),
        life=calculate_insurance(output_score.life),
    )


def calculate_insurance(score_value: OutputScoreEligibility) -> Insurance:
    if not score_value.eligible:
        return Insurance.INELIGIBLE
    if score_value.score <= 0:
        return Insurance.ECONOMIC
    if score_value.score >= 3:
        return Insurance.RESPONSIBLE
    else:
        return Insurance.REGULAR
