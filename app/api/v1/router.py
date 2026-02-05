from fastapi import APIRouter, HTTPException
from app.models.schemas import MemoryResponse, SessionListResponse, AllMemoriesResponse
from app.utils.memory import get_memory
from app.api.v1.endpoints import chat, memory

api_router = APIRouter()

api_router.include_router(chat.router, tags=["Chat"])

@api_router.get("/memory", response_model=AllMemoriesResponse, tags=["Admin"])
async def get_all_memories():
    mem_store = get_memory()
    total_sessions = sum(len(sessions) for sessions in mem_store.values())
    
    return AllMemoriesResponse(
        total_users=len(mem_store),
        total_sessions=total_sessions,
        memories=mem_store
    )