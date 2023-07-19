#-*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
    page = """
    <html>
        <body>
            <h2>카카오 챗봇빌더 스킬 예제입니다</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=page, status_code=200)


@app.post("/skill/hello")
async def skill(req: ChatbotRequest):
    logger.info("user={} intent={} utterance={}".format(
        req.userRequest.user.id,
        req.intent.name,
        req.userRequest.utterance))

    output = {
        'version': '2.0',
        'template': {
            'outputs': [
                {
                    "simpleText": {
                        "text": "안녕하세요! 저는 챗봇입니다."
                    }
                },
                {
                    "simpleText": {
                        "text": "어떤 카드를 보여드릴까요?"
                    }
                },
            ],
            "quickReplies": [
                {
                    "messageText": "Basic Card",
                    "action": "message",
                    "label": "Basic Card 보여주세요."
                },
                {
                    "messageText": "Commerce Card",
                    "action": "message",
                    "label": "Commerce Card 보여주세요."
                },
            ]
        }
    }
    return output

@app.post("/skill/basic-card")
async def skill(req: ChatbotRequest):
    logger.info("user={} intent={} utterance={}".format(
        req.userRequest.user.id,
        req.intent.name,
        req.userRequest.utterance))

    output = {
        'version': '2.0',
        'template': {
            'outputs': [
                {
                    "basicCard": {
                        "title": "",
                        "description": "",
                        "thumbnail": {
                            "imageUrl": "https://t1.kakaocdn.net/kakaocorp/kakaocorp/admin/editor/21c5aa9f017900001."
                        },
                        "buttons": [
                            {
                                "label": "더 알아보기",
                                "action": "webLink",
                                "webLinkUrl": "https://www.kakaocorp.com/page/detail/9348"
                            }
                        ]
                    }
                },
            ]
        }
    }
    return output
