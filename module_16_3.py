# -*- coding: utf-8 -*-
# module_16_3.py
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=1, max_length=20,
                                                 description='Enter user name', example='Вася')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=18)]) -> str:
    # Индекс, который нам нужно создать
    user_id = str(int(max(users, key=int)) + 1)
    # Добавляем в словарь
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User №{user_id} is registered."


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter user ID', example='1')],
        username: Annotated[str, Path(min_length=1, max_length=20,
                                      description='Enter user name', example='Вася')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=18)]) -> str:
    # Обновляем словарь
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated."


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter user ID', example='1')]) -> str:
    # Удаляем из словаря
    users.pop(user_id)
    return f"User №{user_id} has been deleted."
