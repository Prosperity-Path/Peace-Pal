from fastapi import FastAPI, Request
from pydantic import BaseModel
from response_content import Content
from emotion_model import PredictEmotion
import datetime
import json

class Message(BaseModel):
    messageId: str
    sender: str
    recipient: str
    subject: str
    message: str

class Reply(Message):
    replyingTo: str

app = FastAPI()

emotion_model = PredictEmotion()

@app.get("/")
async def test_health():
    f = open('triggers.json')
    data = json.load(f)
    f.close()
    return data

@app.post("/first-message")
async def intro_reply(message: Message, request: Request):
    res_content = Content(message, request)
    return Content.intro_message()

@app.post("/new-message")
async def field_new_message(message: Message, request: Request):
    res_content = Content(message, request)
    text = message.message
    emotion_label = emotion_model.label_emotion(text)[0]['label']
    return res_content.emotion_response(emotion_label)

@app.post("/reply")
async def field_reply(reply: Reply, request: Request):
    res_content = Content(reply, request)
    #TODO: include help handler
    res =  res_content.handle_reply()
    return res

@app.post("/scheduled")
async def scheduled_reply(message: Message, request: Request):
    res_content = Content(message, request)
    payload =  {
        "subject": "Daily Peace Exercise",
        "message":res_content.pick_scheduled_exercise(),
        "sender": message.sender
    }
    # Schedule next message tomorrow
    nowdt = datetime.datetime.now()
    #TODO: logic for time determination
    newdt = nowdt + datetime.timedelta(minutes=3)
    res = res_content.schedule_message(newdt, payload)
    return res

