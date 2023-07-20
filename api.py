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
                    "messageText": "Basic Card 보여주세요",
                    "action": "message",
                    "label": "Basic"
                },
                {
                    "messageText": "Commerce Card 보여주세요",
                    "action": "message",
                    "label": "Commerce"
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
                        "title": "라이언",
                        "description": "덩치는 크지만 마음은 여린 수사자",
                        "thumbnail": {
                            "imageUrl": "https://i.namu.wiki/i/Uk3BUJiR4ovxBg-1R4u3-KgBsHixap3I6typn0q5gR-4WETLzOsZygp9zdJaReCG1gV7cGBHoqJkmBp-gtsUtGcF2hIjLNUjymZ54wc13jAFVasUgjszRK3VKHjGuHdZbj524ZxMPmG5d_NFazqf8g.webp"
                        },
                        "buttons": [
                            {
                                "label": "더 알아보기",
                                "action": "webLink",
                                "webLinkUrl": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                            }
                        ]
                    }
                },
            ]
        }
    }
    return output


@app.post("/skill/commerce-card")
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
                    "commerceCard": {
                        "title": "",
                        "description": "두 뺨이 발그레😊 매일쓰는 칫솔을 깨끗하게!",
                        "price": 30000,
                        "discountRate": 20,
                        "discountedPrice": 23000,
                        "currency": "won",
                        "buttons": [
                            {
                                "label": "구매하기",
                                "action": "webLink",
                                "webLinkUrl": "https://store.kakaofriends.com/products/9959"
                            }
                        ]
                    }
                },
            ]
        }
    }
    return output
