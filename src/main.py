import logging

from fastapi import FastAPI

from src.controllers.handler import get_insurances
from src.models.user import UserInput, UserOutput

app = FastAPI()
logger = logging.getLogger(__name__)


@app.post("/check/")
def create_item(user_input: UserInput) -> UserOutput:
    logger.debug(f"Received {user_input}")
    return get_insurances(user_input=user_input)
