from nonebot import *
from nonebot.adapters.onebot.v11 import *
from nonebot.adapters.onebot.v11.helpers import Cooldown
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata

import time
import requests
import re
import json
import urllib
import random

from .api import BaiduImageAPI
from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

__plugin_meta__ = PluginMetadata(
    name='Baidu Image Search',
    description='',
    usage=""".bdimg <text> [*multipler]:
    使用百度图片搜索text，并随机返回multipler个结果"""
)

bdimg = on_command(('bdimg'), aliases={'bee', 'rbee'}, block=True)

api = BaiduImageAPI()

@bdimg.handle(parameterless=[Cooldown(cooldown=20, prompt='没完没了了是吧')])
async def _(arg: Message = CommandArg()):
    s = ''.join(re.split(r'\*\d{1,2}', arg.extract_plain_text()))
    count = 1

    if r := re.search(r'\*(\d{1,2})', arg.extract_plain_text()):
        if len(r.groups()) > 2:
            await bdimg.finish("[ERROR] Multiple counts found")
        count = int(r.group(1))

    if count > config.MAX_SAMPLES:
        await bdimg.finish(f"[ERROR] Counts greater than {config.MAX_SAMPLES} is not allowed")

    res = api.search(s)

    if len(res) < count:
        await bdimg.finish("[ERROR] Count out of range")

    for i in random.sample(res, count):
        await bdimg.send(MessageSegment.image(i['thumbURL']))
    

