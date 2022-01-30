from fastapi import FastAPI

from src.controllers.calculate_insurance import validation
from src.models.models import UserInput, UserOutput

app = FastAPI()


@app.post("/check/")
async def create_item(user_input: UserInput) -> UserOutput:
    return validation(user_input)
