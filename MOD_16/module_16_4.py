from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/users')
async def get_user_page() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def user_register(user: User, username: str, age: int):
    len_user = len(users)
    if len_user == 0:
        user.id = 1
    else:
        user.id = users[-1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    raise1 = True
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    if raise1:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        del_user = next(user for user in users if user.id == user_id)
        users.remove(del_user)
        return f'User {user_id} has been deleted.'
    except Exception:
        raise HTTPException(status_code=404, detail='User not found')
