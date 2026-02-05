from fastapi import APIRouter, HTTPException
import logging
from datetime import datetime
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat")
logger = logging.getLogger(__name__)

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        session_id = request.session_id or "default"

        reply = await ChatService.generate_openai_response(
            user_id=request.user_id,
            message=request.message,
            session_id=session_id
        )

        return ChatResponse(
            response=reply,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            session_id=session_id
        )

    except Exception:
        logger.exception("Chat error")
        raise HTTPException(500, "Internal assistant error")