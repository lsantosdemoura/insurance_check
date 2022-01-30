from enum import Enum


class Insurance(Enum):
    ECONOMIC = "economic"
    REGULAR = "regular"
    RESPONSIBLE = "responsible"
    INELIGIBLE = "ineligible"


class HouseOwnershipStatus(Enum):
    OWNED = "owned"
    MORTGAGED = "mortgaged"


class MaritalStatus(Enum):
    SINGLE = "single"
    MARRIED = "married"
