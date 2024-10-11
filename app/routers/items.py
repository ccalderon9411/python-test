from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
def read_items():
    return [{"item_name": "Item1"}, {"item_name": "Item2"}]

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}