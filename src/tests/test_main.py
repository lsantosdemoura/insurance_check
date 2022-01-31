import pytest
from black import json
from fastapi.testclient import TestClient

from src.main import app
from src.tests.helpers.e2e_test_cases import test_cases

client = TestClient(app)


@pytest.mark.parametrize("user_input,expected_user_output", test_cases)
def test_e2e_input_and_expected_value(user_input, expected_user_output):
    response = client.post(
        "/check/",
        data=user_input.json(),
    )

    assert response.status_code == 200
    assert response.json() == json.loads(expected_user_output.json())
