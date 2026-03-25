from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str


class GetUsersResponse(BaseModel):
    message: str
    users: list[User]


class GetUserResponse(BaseModel):
    message: str
    user: Optional[User] = None


class CreateUserData(BaseModel):
    name: str


class CreateUserResponse(BaseModel):
    message: str
    user: User


class UpdateUserData(BaseModel):
    name: str


class UpdateUserResponse(BaseModel):
    message: str
    user: Optional[User] = None


class DeleteUserResponse(BaseModel):
    message: str
    users: list[User]
    user: Optional[User] = None
