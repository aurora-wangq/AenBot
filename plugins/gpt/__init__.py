import openai
from nonebot import *
from nonebot.adapters.onebot.v11 import *
import time
import requests
import json
import urllib
from nonebot.params import CommandArg
import random
from nonebot.adapters.onebot.v11.helpers import Cooldown
chat = on_message()
@chat.handle()
async def _(event:Event):
    openai.api_key=""
    messages = []
    message = event.get_message().extract_plain_text()
    user_message_dict = {
        "role": "user",
        "content": message
    }
    messages.append(user_message_dict)
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    # print(response)
    reply = response["choices"][0]["message"]["content"]
    await chat.finish(MessageSegment.text(reply))
