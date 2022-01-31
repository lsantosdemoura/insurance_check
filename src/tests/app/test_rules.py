from datetime import date

import pytest

from src.app.rules import (
    age_above_30_below_40,
    age_above_60,
    age_below_30,
    does_not_have_a_house,
    does_not_have_a_vehicle,
    does_not_have_income,
    has_dependents,
    income_above_200k,
    is_married,
    mortgaged_house,
    vehicle_older_than_5_years,
)
from src.models.enums import HouseOwnershipStatus, MaritalStatus
from src.models.models import House, UserScore, UserScoreEligibility, Vehicle


def test_user_age_above_60_removes_eligibillity_from_disability_and_life(
    user_input_base, user_score_1_risk_base
):
    user_input_base.age = 61
    age_above_60(user_input=user_input_base, user_score=user_score_1_risk_base)
    assert user_score_1_risk_base.disability.eligible is False
    assert user_score_1_risk_base.life.eligible is False


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_age_below_30_decreases_2_from_all_insurances(
    user_input_base, user_score_base
):
    user_input_base.age = 29
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    age_below_30(user_input=user_input_base, user_score=user_score)
    assert user_score.disability.score == (user_score_base - 2)
    assert user_score.auto.score == (user_score_base - 2)
    assert user_score.home.score == (user_score_base - 2)
    assert user_score.life.score == (user_score_base - 2)


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_age_above_30_below_40_decreases_1_from_all_insurances(
    user_input_base, user_score_base
):
    user_input_base.age = 31
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    age_above_30_below_40(user_input=user_input_base, user_score=user_score)
    assert user_score.disability.score == (user_score_base - 1)
    assert user_score.auto.score == (user_score_base - 1)
    assert user_score.home.score == (user_score_base - 1)
    assert user_score.life.score == (user_score_base - 1)


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_has_dependents_increases_1_from_disability_and_life(
    user_input_base, user_score_base
):
    user_input_base.dependents = 1
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    has_dependents(user_input=user_input_base, user_score=user_score)
    assert user_score.disability.score == (user_score_base + 1)
    assert user_score.life.score == (user_score_base + 1)


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_is_married_increases_1_from_life_and_decreases_1_from_disability(
    user_input_base, user_score_base
):
    user_input_base.marital_status = MaritalStatus.MARRIED
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    is_married(user_input=user_input_base, user_score=user_score)
    assert user_score.disability.score == (user_score_base - 1)
    assert user_score.life.score == (user_score_base + 1)


def test_user_does_not_have_income_removes_eligibillity_from_disability(
    user_input_base, user_score_1_risk_base
):
    does_not_have_income(
        user_input=user_input_base, user_score=user_score_1_risk_base
    )
    assert user_score_1_risk_base.disability.eligible is False


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_income_above_200k_decreases_1_from_all_insurances(
    user_input_base, user_score_base
):
    user_input_base.income = 200001
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    income_above_200k(user_input=user_input_base, user_score=user_score)
    assert user_score.disability.score == (user_score_base - 1)
    assert user_score.auto.score == (user_score_base - 1)
    assert user_score.home.score == (user_score_base - 1)
    assert user_score.life.score == (user_score_base - 1)


def test_user_does_not_have_a_house_removes_eligibillity_from_home_insurance(
    user_input_base, user_score_1_risk_base
):
    does_not_have_a_house(
        user_input=user_input_base, user_score=user_score_1_risk_base
    )
    assert user_score_1_risk_base.home.eligible is False


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_has_mortgaged_house_increases_1_from_disability_and_home(
    user_input_base, user_score_base
):
    user_input_base.house = House(
        ownership_status=HouseOwnershipStatus.MORTGAGED
    )
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    mortgaged_house(user_input=user_input_base, user_score=user_score)
    assert user_score.disability.score == (user_score_base + 1)
    assert user_score.home.score == (user_score_base + 1)


def test_user_does_not_have_a_vehicle_removes_eligibillity_from_auto_insurance(
    user_input_base, user_score_1_risk_base
):
    does_not_have_a_vehicle(
        user_input=user_input_base, user_score=user_score_1_risk_base
    )
    assert user_score_1_risk_base.auto.eligible is False


@pytest.mark.parametrize("user_score_base", [1, 2, 3])
def test_user_vehicle_older_than_5_years_increase_1_from_auto(
    user_input_base, user_score_base
):
    user_input_base.vehicle = Vehicle(year=date.today().year - 6)
    user_score = UserScore(
        auto=UserScoreEligibility(score=user_score_base),
        disability=UserScoreEligibility(score=user_score_base),
        home=UserScoreEligibility(score=user_score_base),
        life=UserScoreEligibility(score=user_score_base),
    )
    vehicle_older_than_5_years(
        user_input=user_input_base, user_score=user_score
    )
    assert user_score.auto.score == (user_score_base + 1)
