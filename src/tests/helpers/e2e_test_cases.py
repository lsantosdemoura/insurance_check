from datetime import date

from src.models.enums import HouseOwnershipStatus, Insurance, MaritalStatus
from src.models.user import House, UserInput, UserOutput, Vehicle

test_cases = [
    (
        UserInput(
            age=0,
            dependents=0,
            income=0,
            marital_status=MaritalStatus.SINGLE,
            risk_questions=[False, False, False],
        ),
        UserOutput(
            auto=Insurance.INELIGIBLE,
            disability=Insurance.INELIGIBLE,
            home=Insurance.INELIGIBLE,
            life=Insurance.ECONOMIC,
        ),
    ),
    (
        UserInput(
            age=61,
            dependents=0,
            income=0,
            marital_status=MaritalStatus.SINGLE,
            risk_questions=[False, False, False],
        ),
        UserOutput(
            auto=Insurance.INELIGIBLE,
            disability=Insurance.INELIGIBLE,
            home=Insurance.INELIGIBLE,
            life=Insurance.INELIGIBLE,
        ),
    ),
    (
        UserInput(
            age=29,
            dependents=0,
            income=0,
            marital_status=MaritalStatus.SINGLE,
            risk_questions=[False, False, False],
        ),
        UserOutput(
            auto=Insurance.INELIGIBLE,
            disability=Insurance.INELIGIBLE,
            home=Insurance.INELIGIBLE,
            life=Insurance.ECONOMIC,
        ),
    ),
    (
        UserInput(
            age=31,
            dependents=0,
            income=0,
            marital_status=MaritalStatus.SINGLE,
            risk_questions=[False, False, False],
        ),
        UserOutput(
            auto=Insurance.INELIGIBLE,
            disability=Insurance.INELIGIBLE,
            home=Insurance.INELIGIBLE,
            life=Insurance.ECONOMIC,
        ),
    ),
    (
        UserInput(
            age=31,
            dependents=2,
            income=100000,
            marital_status=MaritalStatus.SINGLE,
            risk_questions=[False, False, False],
            house=House(ownership_status=HouseOwnershipStatus.MORTGAGED),
        ),
        UserOutput(
            auto=Insurance.INELIGIBLE,
            disability=Insurance.REGULAR,
            home=Insurance.ECONOMIC,
            life=Insurance.ECONOMIC,
        ),
    ),
    (
        UserInput(
            age=31,
            dependents=2,
            income=300000,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[True, True, True],
            house=House(ownership_status=HouseOwnershipStatus.MORTGAGED),
        ),
        UserOutput(
            auto=Insurance.INELIGIBLE,
            disability=Insurance.REGULAR,
            home=Insurance.REGULAR,
            life=Insurance.RESPONSIBLE,
        ),
    ),
    (
        UserInput(
            age=31,
            dependents=2,
            income=300000,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[True, True, True],
            house=House(ownership_status=HouseOwnershipStatus.MORTGAGED),
            vehicle=Vehicle(year=date.today().year),
        ),
        UserOutput(
            auto=Insurance.REGULAR,
            disability=Insurance.REGULAR,
            home=Insurance.REGULAR,
            life=Insurance.RESPONSIBLE,
        ),
    ),
    (
        UserInput(
            age=31,
            dependents=2,
            income=300000,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[True, True, True],
            house=House(ownership_status=HouseOwnershipStatus.OWNED),
            vehicle=Vehicle(year=date.today().year - 6),
        ),
        UserOutput(
            auto=Insurance.REGULAR,
            disability=Insurance.REGULAR,
            home=Insurance.REGULAR,
            life=Insurance.RESPONSIBLE,
        ),
    ),
    (
        UserInput(
            age=35,
            dependents=2,
            income=0,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[False, True, False],
            house=House(ownership_status=HouseOwnershipStatus.OWNED),
            vehicle=Vehicle(year=2005),
        ),
        UserOutput(
            auto=Insurance.ECONOMIC,
            disability=Insurance.INELIGIBLE,
            home=Insurance.ECONOMIC,
            life=Insurance.REGULAR,
        ),
    ),
    (
        UserInput(
            age=35,
            dependents=2,
            income=0,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[False, True, False],
            house=House(ownership_status=HouseOwnershipStatus.OWNED),
            vehicle=Vehicle(year=2021),
        ),
        UserOutput(
            auto=Insurance.REGULAR,
            disability=Insurance.INELIGIBLE,
            home=Insurance.ECONOMIC,
            life=Insurance.REGULAR,
        ),
    ),
    (
        UserInput(
            age=30,
            dependents=2,
            income=0,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[False, True, False],
            house=House(ownership_status=HouseOwnershipStatus.OWNED),
            vehicle=Vehicle(year=2021),
        ),
        UserOutput(
            auto=Insurance.REGULAR,
            disability=Insurance.INELIGIBLE,
            home=Insurance.ECONOMIC,
            life=Insurance.REGULAR,
        ),
    ),
]
