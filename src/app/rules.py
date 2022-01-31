from datetime import date

from src.models.enums import HouseOwnershipStatus, MaritalStatus
from src.models.models import UserInput, UserScore


def age_above_60(user_input: UserInput, user_score: UserScore) -> UserScore:
    if user_input.age > 60:
        user_score.disability.eligible = False
        user_score.life.eligible = False
    return user_score


def age_below_30(user_input: UserInput, user_score: UserScore) -> UserScore:
    if user_input.age < 30:
        user_score.disability.score -= 2
        user_score.auto.score -= 2
        user_score.home.score -= 2
        user_score.life.score -= 2
    return user_score


def age_above_30_below_40(
    user_input: UserInput, user_score: UserScore
) -> UserScore:
    if user_input.age > 30 and user_input.age < 40:
        user_score.disability.score -= 1
        user_score.auto.score -= 1
        user_score.home.score -= 1
        user_score.life.score -= 1
    return user_score


def has_dependents(user_input: UserInput, user_score: UserScore) -> UserScore:
    if user_input.dependents:
        user_score.disability.score += 1
        user_score.life.score += 1
    return user_score


def is_married(user_input: UserInput, user_score: UserScore) -> UserScore:
    if user_input.marital_status == MaritalStatus.MARRIED:
        user_score.life.score += 1
        user_score.disability.score -= 1
    return user_score


def does_not_have_income(
    user_input: UserInput, user_score: UserScore
) -> UserScore:
    if not user_input.income:
        user_score.disability.eligible = False
    return user_score


def income_above_200k(
    user_input: UserInput, user_score: UserScore
) -> UserScore:
    if user_input.income > 200000:
        user_score.disability.score -= 1
        user_score.auto.score -= 1
        user_score.home.score -= 1
        user_score.life.score -= 1

    return user_score


def does_not_have_a_house(
    user_input: UserInput, user_score: UserScore
) -> UserScore:
    if not user_input.house:
        user_score.home.eligible = False
    return user_score


def mortgaged_house(user_input: UserInput, user_score: UserScore) -> UserScore:
    if (
        user_input.house
        and user_input.house.ownership_status == HouseOwnershipStatus.MORTGAGED
    ):
        user_score.disability.score += 1
        user_score.home.score += 1
    return user_score


def does_not_have_a_vehicle(
    user_input: UserInput, user_score: UserScore
) -> UserScore:
    if not user_input.vehicle:
        user_score.auto.eligible = False
    return user_score


def vehicle_older_than_5_years(
    user_input: UserInput, user_score: UserScore
) -> UserScore:
    if user_input.vehicle and user_input.vehicle.year < (
        date.today().year - 5
    ):
        user_score.auto.score += 1
    return user_score
