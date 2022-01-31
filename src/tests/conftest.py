import pytest

from src.models.enums import MaritalStatus
from src.models.models import UserInput, UserScore, UserScoreEligibility


@pytest.fixture
def user_score_1_risk_base():
    return UserScore(
        auto=UserScoreEligibility(score=1),
        disability=UserScoreEligibility(score=1),
        home=UserScoreEligibility(score=1),
        life=UserScoreEligibility(score=1),
    )


@pytest.fixture
def user_score_2_risk_base():
    return UserScore(
        auto=UserScoreEligibility(score=2),
        disability=UserScoreEligibility(score=2),
        home=UserScoreEligibility(score=2),
        life=UserScoreEligibility(score=2),
    )


@pytest.fixture
def user_score_3_risk_base():
    return UserScore(
        auto=UserScoreEligibility(score=3),
        disability=UserScoreEligibility(score=3),
        home=UserScoreEligibility(score=3),
        life=UserScoreEligibility(score=3),
    )


@pytest.fixture
def user_input_base():
    return UserInput(
        age=0,
        dependents=0,
        income=0,
        marital_status=MaritalStatus.MARRIED,
        risk_questions=[True, True, True],
    )
