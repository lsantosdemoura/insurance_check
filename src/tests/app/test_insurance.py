from unittest import mock

import pytest

from src.app.insurance import (
    _calculate_base_score,
    _calculate_insurance_score,
    calculate_insurance,
)
from src.models.enums import Insurance
from src.models.models import UserScoreEligibility


@pytest.mark.parametrize(
    "risk_questions,expected_value",
    [
        ([True, True, True], 3),
        ([True, True, False], 2),
        ([True, False, False], 1),
    ],
)
def test_calculate_base_score_returns_sum_of_true_values(
    risk_questions, expected_value
):
    user_score = _calculate_base_score(risk_questions=risk_questions)
    user_score.disability.score == expected_value
    user_score.auto.score == expected_value
    user_score.home.score == expected_value
    user_score.life.score == expected_value


def test_calculate_insuranse_calls_all_passed_rules(user_input_base):
    rule_1 = mock.Mock(side_effect=lambda user_input, user_score: user_score)
    rule_2 = mock.Mock(side_effect=lambda user_input, user_score: user_score)
    rules = [rule_1, rule_2]
    calculate_insurance(user_input=user_input_base, rules=rules)
    rule_1.assert_called_once()
    rule_2.assert_called_once()


def test_calculate_insurance_score_returns_ineligible_for_eligible_false():
    score_value = UserScoreEligibility(score=3, eligible=False)
    assert _calculate_insurance_score(score_value) == Insurance.INELIGIBLE


@pytest.mark.parametrize(
    "user_score,expected_insurance",
    [
        (UserScoreEligibility(score=0, eligible=True), Insurance.ECONOMIC),
        (UserScoreEligibility(score=1, eligible=True), Insurance.REGULAR),
        (UserScoreEligibility(score=3, eligible=True), Insurance.RESPONSIBLE),
    ],
)
def test_calculate_insurance_score_returns_correct_for_each_score_range(
    user_score, expected_insurance
):

    assert _calculate_insurance_score(user_score) == expected_insurance
