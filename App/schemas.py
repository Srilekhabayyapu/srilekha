from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    user_input: str
    context: Optional[List[str]] = None

class ChatResponse(BaseModel):
    bot_response: str
    context: Optional[List[str]] = None
