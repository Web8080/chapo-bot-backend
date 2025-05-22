from fastapi import APIRouter, Request
from backend.services import shopping_list_service

router = APIRouter()

@router.post("/shopping-list/add")
async def add_to_list(request: Request):
    data = await request.json()
    items_text = data.get("items", "")
    result = shopping_list_service.add_items_to_shopping_list(items_text)
    return {"message": result}

@router.get("/shopping-list")
async def get_list():
    result = shopping_list_service.get_shopping_list()
    return {"shopping_list": result}

@router.post("/shopping-list/clear")
async def clear_list():
    result = shopping_list_service.clear_shopping_list()
    return {"message": result}

@router.post("/shopping-list/remove")
async def remove_item(request: Request):
    data = await request.json()
    item_text = data.get("item", "")
    result = shopping_list_service.remove_item_from_shopping_list(item_text)
    return {"message": result}
