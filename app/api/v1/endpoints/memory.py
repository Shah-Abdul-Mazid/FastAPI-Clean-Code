from fastapi import APIRouter, HTTPException
from app.utils.memory import get_memory

router = APIRouter(prefix="/v1/endpoints/memory")

@router.get("/{user_id}")
async def get_user_memory(user_id: str):
    memory = get_memory()
    return memory.get(user_id, {})
