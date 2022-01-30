from typing import Callable

from src.models.models import (
    Insurance,
    OutputScore,
    OutputScoreEligibility,
    UserInput,
    UserOutput,
)


def _calculate_base_score(risk_questions) -> OutputScore:
    base_score = sum(risk_questions)

    return OutputScore(
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


def calculate_insurance(
    user_input: UserInput,
    rules: tuple[Callable[[UserInput, OutputScore], OutputScore]],
) -> UserOutput:
    output_score = _calculate_base_score(user_input.risk_questions)
    for rule in rules:
        output_score = rule(user_input, output_score)

    return UserOutput(
        auto=_calculate_insurance_score(output_score.auto),
        home=_calculate_insurance_score(output_score.home),
        disability=_calculate_insurance_score(output_score.disability),
        life=_calculate_insurance_score(output_score.life),
    )


def _calculate_insurance_score(
    score_value: OutputScoreEligibility,
) -> Insurance:
    if not score_value.eligible:
        return Insurance.INELIGIBLE
    if score_value.score <= 0:
        return Insurance.ECONOMIC
    if score_value.score >= 3:
        return Insurance.RESPONSIBLE
    else:
        return Insurance.REGULAR


# create unit tests
# create readme with examples
# and how to run
# explain thinking on readme
# create travis config
# create mutation tests mutpy
#
