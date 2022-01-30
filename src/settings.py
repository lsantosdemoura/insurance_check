from starlette.config import Config

config = Config(".env")
RISK_QUESTIONS_MIN_ITEMS = config(
    "RISK_QUESTIONS_MIN_ITEMS",
    cast=int,
    default=3,
)
RISK_QUESTIONS_MAX_ITEMS = config(
    "RISK_QUESTIONS_MAX_ITEMS",
    cast=int,
    default=3,
)
