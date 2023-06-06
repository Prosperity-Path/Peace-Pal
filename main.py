from fastapi import FastAPI, Request
from pydantic import BaseModel
from response_content import Content
from emotion_model import PredictEmotion
import requests
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

def get_pdk_data(request, url_path):
    pdk_url = request.headers['PDK-URL']
    res = requests.get(pdk_url + url_path)
    return res.json()

def post_pdk_data(request, url_path, payload):
    pdk_url = request.headers['PDK-URL']
    res = requests.post(pdk_url + url_path, payload)
    return res.json()

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

@app.post("/schedule")
async def scheduled_reply(request: Request):
    user_list = get_pdk_data(request, '/users')    
    for user in user_list:
        msg_path = '/messages?recipient=' + user
        msgs_to_user = get_pdk_data(request, msg_path)
        prev_sent_msgs = [m['message'] for m in msgs_to_user]
        message = {
            "subject": "Daily Peace Exercise",
            "recipient": user,
            "message":""
        }
        res_content = Content(message, request)
        message["message"] = res_content.pick_scheduled_exercise(prev_sent_msgs)
        post_pdk_data(request, '/send', message)
    return user_list

