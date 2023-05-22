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

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

chat = on_message()

Message_count = 0
Message_content = ""
Presets = "你叫AenStarAX,你是山东省临沂一中的高一学生。你在一个qq群中,我会给你几条聊天记录,你需要想想在这个聊天记录的情境下AenStarAX接下来会说什么,作为AenStarAX这名学生,AenStarAX会说:“......”，你需要补全“......”代表的内容然后输出这段内容,最重要的是除了输出“......”代表的内容外不要输出其他任何东西,你补全的“......”应该主要与聊天记录的最后三条相关,且符合AenStarAX的人设,你补全聊天的时候应该尽量附和之前的人说的话,你补全的风格应该较为简短且口语化,最重要的是只能是一句话,绝对不要把话说的完整或太长，绝对不要使用书面语言,绝对不能和聊天记录里有相似的句子,以下是提供给你的聊天记录:"

@chat.handle()
async def _(event:Event):
    #return
    global Message_count
    global Message_content
    global Presets
    Message_Check = event.get_message()
    for segment in Message_Check:
        if segment.type != 'image':
            Message_count = Message_count+1
            Message_content += str(Message_count)+"."+event.get_message().extract_plain_text()
            Chat_Standard = random.randint(4,7)
    
            if Message_count >= Chat_Standard:
                openai.api_key=global_config.openai_apikey
                messages = []
                user_message_dict = {"role": "user","content": Presets + Message_content}
                messages.append(user_message_dict)
                response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
                # print(response)
                reply = response["choices"][0]["message"]["content"]
                Message_content = ""
                Message_count = 0
                reply = reply.replace( "\"",'')
                reply = reply.replace( "\"",'')
                reply = reply.replace( "“",'')
                reply = reply.replace( "”",'')
                reply = reply.replace( "。",'')
                reply = reply.replace( "，",' ')
                reply = reply.replace( ",",' ')
                if len(reply) < 20:
                    await chat.send(MessageSegment.text(reply))




