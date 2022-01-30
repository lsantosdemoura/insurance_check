from datetime import date
import operator as op

from src.models.models import (
    HouseOwnershipStatus,
    MaritalStatus,
    OutputScore,
    UserInput,
)


def age_rules(user_input: UserInput, output_score: OutputScore):
    if user_input.age > 60:
        output_score.disability.eligible = False
        output_score.life.eligible = False
    elif user_input.age < 30:
        output_score.disability.score -= 2
        output_score.auto.score -= 2
        output_score.home.score -= 2
        output_score.life.score -= 2
    elif user_input.age < 40:
        output_score.disability.score -= 1
        output_score.auto.score -= 1
        output_score.home.score -= 1
        output_score.life.score -= 1
    return output_score


def dependants_rules(user_input: UserInput, output_score: OutputScore):
    if user_input.dependents:
        output_score.disability.score += 1
        output_score.life.score += 1
    return output_score


def marital_status_rules(user_input: UserInput, output_score: OutputScore):
    if user_input.marital_status == MaritalStatus.MARRIED:
        output_score.life.score += 1
        output_score.disability.score -= 1
    return output_score


def income_rules(user_input: UserInput, output_score: OutputScore):
    if not user_input.income:
        output_score.disability.eligible = False
    elif user_input.income > 200000:
        output_score.disability.score -= 1
        output_score.auto.score -= 1
        output_score.home.score -= 1
        output_score.life.score -= 1

    return output_score


def house_rules(user_input: UserInput, output_score: OutputScore):
    if not user_input.house:
        output_score.home.eligible = False
    elif user_input.house == HouseOwnershipStatus.MORTGAGED:
        output_score.disability.score += 1
        output_score.home.score += 1
    return output_score


def vehicle_rules(user_input: UserInput, output_score: OutputScore):
    if not user_input.vehicle:
        output_score.auto.eligible = False
    elif user_input.vehicle.year < (date.today().year - 5):
        output_score.auto.score += 1
    return output_score


def rule_1(user_input: UserInput, output_score: OutputScore):
    if not user_input.income:
        output_score.disability.eligible = False
    if not user_input.vehicle:
        output_score.auto.eligible = False
    if not user_input.house:
        output_score.home.eligible = False
    return output_score


def rule_2(user_input: UserInput, output_score: OutputScore):
    if user_input.age > 60:
        output_score.disability.eligible = False
        output_score.life.eligible = False
    return output_score


def rule_3(user_input: UserInput, output_score: OutputScore):
    if user_input.age < 30:
        output_score.disability.score -= 2
        output_score.auto.score -= 2
        output_score.home.score -= 2
        output_score.life.score -= 2
    elif user_input.age < 40:
        output_score.disability.score -= 1
        output_score.auto.score -= 1
        output_score.home.score -= 1
        output_score.life.score -= 1
    return output_score


def rule_4(user_input: UserInput, output_score: OutputScore):
    if user_input.income > 200000:
        output_score.disability.score -= 1
        output_score.auto.score -= 1
        output_score.home.score -= 1
        output_score.life.score -= 1
    return output_score


def rule_5(user_input: UserInput, output_score: OutputScore):
    if user_input.house == HouseOwnershipStatus.MORTGAGED:
        output_score.disability.score += 1
        output_score.home.score += 1
    return output_score


def rule_6(user_input: UserInput, output_score: OutputScore):
    if user_input.dependents:
        output_score.disability.score += 1
        output_score.life.score += 1
    return output_score


def rule_7(user_input: UserInput, output_score: OutputScore):
    if user_input.marital_status == MaritalStatus.MARRIED:
        output_score.life.score += 1
        output_score.disability.score -= 1
    return output_score


def rule_8(user_input: UserInput, output_score: OutputScore):
    if user_input.vehicle and user_input.vehicle.year < (
        date.today().year - 5
    ):
        output_score.auto.score += 1
    return output_score
