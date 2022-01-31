import pytest

from src.models.enums import Insurance, MaritalStatus
from src.models.user import (
    UserInput,
    UserOutput,
    UserScore,
    UserScoreEligibility,
)


@pytest.fixture
def user_score_1_risk_base():
    return UserScore(
        auto=UserScoreEligibility(score=1),
        disability=UserScoreEligibility(score=1),
        home=UserScoreEligibility(score=1),
        life=UserScoreEligibility(score=1),
    )


@pytest.fixture
def user_input_base():
    return UserInput(
        age=0,
        dependents=0,
        income=0,
        marital_status=MaritalStatus.SINGLE,
        risk_questions=[False, False, False],
    )


@pytest.fixture
def user_output_base():
    return UserOutput(
        auto=Insurance.INELIGIBLE,
        disability=Insurance.INELIGIBLE,
        home=Insurance.INELIGIBLE,
        life=Insurance.ECONOMIC,
    )
