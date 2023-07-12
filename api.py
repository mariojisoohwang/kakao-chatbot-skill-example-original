from fastapi import FastAPI
import logging
from dto import ChatbotRequest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('main')


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
                    { 'simpleText': msg }
                ]
            }
    }

    return simple_text_output
