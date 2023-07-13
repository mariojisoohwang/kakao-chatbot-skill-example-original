#-*- coding: utf-8 -*-

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
    return "카카오 챗봇빌더 스킬 예제입니다!"

@app.post("/skill")
async def skill(req: ChatbotRequest):

    logger.info("user={} intent={} utterance={}".format(
        req.userRequest.user.id,
        req.intent.name,
        req.userRequest.utterance))

    output = {
        'version': '2.0',
        'template': {
            'outputs': [
                { 'simpleText': "안녕하세요! 저는 챗봇입니다."},
                { 'simpleText': "어떤 이야기를 나눌까요?"}
            ]
        }
    }
    return output
