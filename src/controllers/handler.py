from src.app.insurance import calculate_insurance
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
from src.models.models import UserInput, UserOutput


def get_insurances(user_input: UserInput) -> UserOutput:
    return calculate_insurance(
        user_input=user_input,
        rules=(
            age_above_60,
            age_below_30,
            age_above_30_below_40,
            does_not_have_a_vehicle,
            has_dependents,
            income_above_200k,
            is_married,
            does_not_have_a_house,
            does_not_have_income,
            mortgaged_house,
            vehicle_older_than_5_years,
        ),
    )
