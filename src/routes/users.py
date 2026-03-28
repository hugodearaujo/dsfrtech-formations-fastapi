from fastapi import APIRouter
from ..schemas.users import (
    GetUsersResponse,
    GetUserResponse,
    CreateUserData,
    CreateUserResponse,
    UpdateUserData,
    UpdateUserResponse,
    DeleteUserResponse,
)

users_router = APIRouter(prefix="/users", tags=["users"])


users_data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
]


# Get All
@users_router.get("", status_code=200, response_model=GetUsersResponse)
async def get_users():
    return {
        "message": "List of users",
        "users": users_data,
    }


# Get One
@users_router.get("/{user_id}", status_code=200, response_model=GetUserResponse)
async def get_user(user_id: int):
    for user in users_data:
        if user["id"] == user_id:
            return {
                "message": f"User with ID {user_id}",
                "user": user,
            }
    return {
        "message": f"User with ID {user_id} not found",
        "user": None,
    }


# Create One
@users_router.post("", status_code=201, response_model=CreateUserResponse)
async def create_user(data: CreateUserData):
    new_user = {"id": len(users_data) + 1, "name": data.name, "age": data.age}
    users_data.append(new_user)
    return {"message": "User created", "user": new_user}


# Update One
@users_router.put("/{user_id}", status_code=200, response_model=UpdateUserResponse)
async def update_user(user_id: int, data: UpdateUserData):
    for user in users_data:
        if user["id"] == user_id:
            user["name"] = data.name
            user["age"] = data.age
            return {"message": f"User with ID {user_id} updated", "user": user}
    return {"message": f"User with ID {user_id} not found", "user": None}


# Delete One
@users_router.delete("/{user_id}", status_code=202, response_model=DeleteUserResponse)
async def delete_user(user_id: int):
    for user in users_data:
        if user["id"] == user_id:
            users_data.remove(user)
            return {
                "message": f"User with ID {user_id} deleted",
                "users": users_data,
                "user": user,
            }
    return {
        "message": f"User with ID {user_id} not found",
        "users": users_data,
        "user": None,
    }
