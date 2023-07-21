from copy import deepcopy
from fastapi import FastAPI, Body
from config import DB_USERNAME, DB_PASSWORD, DB_PORT, DB_NAME, DB_HOST

from tortoise.contrib.fastapi import register_tortoise

from service import WriteNewCargoToDatasbase, NewCargoResponse

app = FastAPI()


@app.post("/")
async def NewCargo(payload: dict = Body(...)):
    await WriteNewCargoToDatasbase(payload)
    response = await NewCargoResponse(deepcopy(payload))
    return response

register_tortoise(
    app,
    db_url=f'postgres://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
