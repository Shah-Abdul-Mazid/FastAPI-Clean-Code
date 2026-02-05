from datetime import datetime
from openai import OpenAI

from app.utils.memory import get_memory, save_memory

client = OpenAI()  

class ChatService:
    @staticmethod
    async def generate_openai_response(
        user_id: str,
        message: str,
        session_id: str = "default"
    ) -> str:

        memory = get_memory()
        memory.setdefault(user_id, {}).setdefault(session_id, [])
        history = memory[user_id][session_id]

        messages = [
            {"role": "system", "content": "You are a personalized assistant who remembers user details."}
        ]

        for entry in history[-10:]:
            messages.append({
                "role": entry["role"],
                "content": entry["message"]
            })

        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=messages
        )

        bot_reply = response.choices[0].message.content
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        history.extend([
            {"role": "user", "message": message, "timestamp": timestamp},
            {"role": "assistant", "message": bot_reply, "timestamp": timestamp}
        ])

        save_memory(memory)
        return bot_reply