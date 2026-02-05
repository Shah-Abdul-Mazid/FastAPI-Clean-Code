from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    timestamp: str
    session_id: str

class MemoryResponse(BaseModel):
    user_id: str
    session_id: str
    conversation_history: List[Dict]

class SessionListResponse(BaseModel):
    user_id: str
    sessions: List[str]

class AllMemoriesResponse(BaseModel):
    total_users: int
    total_sessions: int
    memories: Dict
