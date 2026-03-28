from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    name: str
    classification: str
    min_qnt: int
    max_qnt: int


class GetItemsResponse(BaseModel):
    message: str
    items: list[Item]


class GetItemResponse(BaseModel):
    message: str
    item: Optional[Item] = None


class CreateItemData(BaseModel):
    name: str
    classification: str
    min_qnt: int
    max_qnt: int


class CreateItemResponse(BaseModel):
    message: str
    item: Item


class UpdateItemData(BaseModel):
    name: str
    classification: str
    min_qnt: int
    max_qnt: int


class UpdateItemResponse(BaseModel):
    message: str
    item: Optional[Item] = None


class DeleteItemResponse(BaseModel):
    message: str
    items: list[Item]
    item: Optional[Item] = None
