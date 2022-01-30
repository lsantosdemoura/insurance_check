from datetime import date

from src.models.models import (
    HouseOwnershipStatus,
    MaritalStatus,
    OutputScore,
    UserInput,
)


def age_above_60(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.age > 60:
        output_score.disability.eligible = False
        output_score.life.eligible = False
    return output_score


def age_below_30(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.age < 30:
        output_score.disability.score -= 2
        output_score.auto.score -= 2
        output_score.home.score -= 2
        output_score.life.score -= 2
    return output_score


def age_above_thirty_below_40(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.age > 30 and user_input.age < 40:
        output_score.disability.score -= 1
        output_score.auto.score -= 1
        output_score.home.score -= 1
        output_score.life.score -= 1
    return output_score


def has_dependents(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.dependents:
        output_score.disability.score += 1
        output_score.life.score += 1
    return output_score


def is_married(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.marital_status == MaritalStatus.MARRIED:
        output_score.life.score += 1
        output_score.disability.score -= 1
    return output_score


def does_not_have_income(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if not user_input.income:
        output_score.disability.eligible = False
    return output_score


def income_above_200k(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.income > 200000:
        output_score.disability.score -= 1
        output_score.auto.score -= 1
        output_score.home.score -= 1
        output_score.life.score -= 1

    return output_score


def does_not_have_a_house(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if not user_input.house:
        output_score.home.eligible = False
    return output_score


def mortgaged_house(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.house == HouseOwnershipStatus.MORTGAGED:
        output_score.disability.score += 1
        output_score.home.score += 1
    return output_score


def does_not_have_a_vehicle(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if not user_input.vehicle:
        output_score.auto.eligible = False
    return output_score


def vehicle_older_than_5_years(
    user_input: UserInput, output_score: OutputScore
) -> OutputScore:
    if user_input.vehicle and user_input.vehicle.year < (
        date.today().year - 5
    ):
        output_score.auto.score += 1
    return output_score
