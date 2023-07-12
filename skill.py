from fastapi import FastAPI
from pydantic import BaseModel
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('main')


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


app = FastAPI()

@app.get("/")
async def home():
    return "Kakao Chatbot Skill Example"

@app.post("/skill")
async def skill(req: ChatbotRequest):

    msg = 'Hello!'

    simple_text_output = {
        'version': '2.0',
            'template': {
                'outputs': [
                    {'simpleText': msg}
                ]
            }
    }

    return simple_text_output
