from fastapi import APIRouter
from ..schemas.items import (
    GetItemsResponse,
    GetItemResponse,
    CreateItemData,
    CreateItemResponse,
    UpdateItemData,
    UpdateItemResponse,
    DeleteItemResponse,
)

items_router = APIRouter(prefix="/items", tags=["items"])


items_data = [
    {"id": 1, "name": "Banana", "classification": "fruit", "min_qnt": 10, "max_qnt": 100},
    {"id": 2, "name": "Chocolate", "classification": "snack", "min_qnt": 5, "max_qnt": 50},
    {"id": 3, "name": "Carne", "classification": "Proteina", "min_qnt": 1, "max_qnt": 20},
]


@items_router.get("", status_code=200, response_model=GetItemsResponse)
async def get_items():
    return {
        "message": "List of items",
        "items": items_data,
    }


@items_router.get("/{item_id}", status_code=200, response_model=GetItemResponse)
async def get_item(item_id: int):
    for item in items_data:
        if item["id"] == item_id:
            return {
                "message": f"Item with ID {item_id}",
                "item": item,
            }
    return {
        "message": f"Item with ID {item_id} not found",
        "item": None,
    }


@items_router.post("", status_code=201, response_model=CreateItemResponse)
async def create_item(data: CreateItemData):
    new_item = {
        "id": len(items_data) + 1,
        "name": data.name,
        "classification": data.classification,
        "min_qnt": data.min_qnt,
        "max_qnt": data.max_qnt,
    }
    items_data.append(new_item)
    return {"message": "Item created", "item": new_item}


@items_router.put("/{item_id}", status_code=200, response_model=UpdateItemResponse)
async def update_item(item_id: int, data: UpdateItemData):
    for item in items_data:
        if item["id"] == item_id:
            item["name"] = data.name
            item["classification"] = data.classification
            item["min_qnt"] = data.min_qnt
            item["max_qnt"] = data.max_qnt
            return {"message": f"Item with ID {item_id} updated", "item": item}
    return {"message": f"Item with ID {item_id} not found", "item": None}


@items_router.delete("/{item_id}", status_code=202, response_model=DeleteItemResponse)
async def delete_item(item_id: int):
    for item in items_data:
        if item["id"] == item_id:
            items_data.remove(item)
            return {
                "message": f"Item with ID {item_id} deleted",
                "items": items_data,
                "item": item,
            }
    return {
        "message": f"Item with ID {item_id} not found",
        "items": items_data,
        "item": None,
    }
