import json
import os
from typing import Dict, Any

DB_PATH = "chat_memory.json"

def get_memory() -> Dict[str, Any]:

    if not os.path.exists(DB_PATH):
        return {}
    
    try:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}

def save_memory(data: Dict[str, Any]):

    try:
        with open(DB_PATH, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving memory to file: {e}")

def clear_memory():

    save_memory({})