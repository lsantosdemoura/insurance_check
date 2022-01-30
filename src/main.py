from fastapi import FastAPI

from src.controllers.handler import get_insurances
from src.models.models import UserInput, UserOutput

app = FastAPI()


@app.post("/check/")
async def create_item(user_input: UserInput) -> UserOutput:
    return get_insurances(user_input=user_input)
