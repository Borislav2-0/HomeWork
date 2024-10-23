from fastapi import FastAPI

app = FastAPI()
users = {'1': "Name: Example, age: 21"}


@app.get('/users')
async def get_user() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    user_id = str(max([int(key) for key in users.keys()]) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_data_user(user_id: str, username: str, age: int) -> str:
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"The user {user_id} is registered"
    else:
        return f"User {user_id} not found"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return 'User was deleted'