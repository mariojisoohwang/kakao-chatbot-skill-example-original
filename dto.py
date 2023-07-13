from pydantic import BaseModel
from typing import Optional


class UserProperty(BaseModel):
    plusfriendUserKey: str

class User(BaseModel):
    id: str
    properties: UserProperty

class UserRequest(BaseModel):
    utterance: str
    callbackUrl: Optional[str]
    user: User

class Intent(BaseModel):
    name: str

class ChatbotRequest(BaseModel):
    userRequest: UserRequest
    intent: Intent

