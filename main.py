# pylint: disable=E0611,E0401
from typing import List

from fastapi import FastAPI, HTTPException, Request, Body
# from models import User_Pydantic, UserIn_Pydantic, Users, 
from models import Cargo, CargoDate
from pydantic import BaseModel
from config import DB_USERNAME, DB_PASSWORD, DB_PORT, DB_NAME

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()


class Status(BaseModel):
    message: str


# @app.get("/users", response_model=List[User_Pydantic])
# async def get_users():
#     return await User_Pydantic.from_queryset(Users.all())
# @app.post("/users", response_model=User_Pydantic)
# async def create_user(user: UserIn_Pydantic):
#     user_obj = await Users.create(**user.dict(exclude_unset=True))
#     return await User_Pydantic.from_tortoise_orm(user_obj)


# @app.get(
#     "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
# )
# async def get_user(user_id: int):
#     return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


# @app.put(
#     "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
# )
# async def update_user(user_id: int, user: UserIn_Pydantic):
#     await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
#     return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


# @app.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
# async def delete_user(user_id: int):
#     deleted_count = await Users.filter(id=user_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#     return Status(message=f"Deleted user {user_id}")

@app.post("/")
async def get_body(payload: dict = Body(...)):
    for date in payload:
        print(date)
        # if CargoDate.get(date=date):
        cargo_date = await CargoDate.get(date=date)
        # else:
        # cargo_date = await CargoDate.create(date=date)
        print(cargo_date.id)
        for cargo in payload[date]:
            print(cargo)
            await Cargo.create(
                cargo_date_id=cargo_date.id,
                # cargo_type=cargo.cargo_type,
                # cargo_rate=cargo.rate,
            )
    return payload

register_tortoise(
    app,
    db_url= f'postgres://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}',
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)