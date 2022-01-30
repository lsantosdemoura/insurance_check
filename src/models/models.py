from datetime import date
from typing import Optional

from pydantic import BaseModel, conint, conlist

from src import settings
from src.models.enums import HouseOwnershipStatus, Insurance, MaritalStatus


class House(BaseModel):
    ownership_status: HouseOwnershipStatus


class Vehicle(BaseModel):
    year: conint(
        ge=1886, le=date.today().year  # the first car was invented in 1886
    )


class UserInput(BaseModel):
    age: conint(ge=0)
    dependents: conint(ge=0)
    income: conint(ge=0)
    marital_status: MaritalStatus
    risk_questions: conlist(
        bool,
        min_items=settings.RISK_QUESTIONS_MIN_ITEMS,
        max_items=settings.RISK_QUESTIONS_MAX_ITEMS,
    )
    house: Optional[House]
    vehicle: Optional[Vehicle]


class UserOutput(BaseModel):
    auto: Insurance
    disability: Insurance
    home: Insurance
    life: Insurance


class UserScoreEligibility(BaseModel):
    score: int
    eligible: bool = True


class UserScore(BaseModel):
    auto: UserScoreEligibility
    disability: UserScoreEligibility
    home: UserScoreEligibility
    life: UserScoreEligibility
