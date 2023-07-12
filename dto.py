from pydantic import BaseModel


class UserProperty(BaseModel):
    plusfriendUserKey: str

class User(BaseModel):
    id: str
    properties: UserProperty

class UserRequest(BaseModel):
    utterance: str
    callbackUrl: str
    user: User

class Intent(BaseModel):
    name: str

class ChatbotRequest(BaseModel):
    userRequest: UserRequest
    intent: Intent

