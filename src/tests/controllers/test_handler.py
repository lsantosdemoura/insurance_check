from unittest import mock

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
    vehicle_newer_than_5_years,
)
from src.controllers.handler import get_insurances


@mock.patch("src.controllers.handler.calculate_insurance")
def test_get_insurances_calls_calculate_insurance_with_all_rules(
    mock_calculate_insurance, user_input_base
):
    get_insurances(user_input=user_input_base)
    mock_calculate_insurance.assert_called_with(
        user_input=user_input_base,
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
            vehicle_newer_than_5_years,
        ),
    )
