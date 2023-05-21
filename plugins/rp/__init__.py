from nonebot import on_command, get_driver
from datetime import datetime
from nonebot.adapters.onebot.v11 import *
from nonebot.plugin import PluginMetadata

import json
import hashlib
import random
import os

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

db = []

__plugin_meta__ = PluginMetadata(
    name="RP Calculator",
    description="",
    usage=""".rp 获取今日RP"""
)

try:
    with open(config.DATABASE_PATH, 'r', encoding='utf8') as f:
        db = json.loads(f.read())
except FileNotFoundError:
    db = [
        {
            'range': [ 0, 100 ],
            'text': 'This is an initial prompt. Add custom prompts to db.json'
        }
    ]
    if not config.WORKDIR.exists():
        os.makedirs(config.WORKDIR)
    with open(config.DATABASE_PATH, 'w', encoding='utf8') as f:
        f.write(json.dumps(db, ensure_ascii=False, indent=4))

rp = on_command("rp", block=True)

def get_rp(userid):
    date = datetime.today()
    s = f"{date.year}||{date.month}||{date.day}@@{userid}"
    hash = hashlib.md5(s.encode('utf8')).hexdigest()
    return int(hash, 16) % 100 + 1

@rp.handle()
async def _(event: Event):
    x = get_rp(event.user_id)
    s = [ i['text'] for i in db if i['range'][0] <= x and x <= i['range'][1] ]
    params = {
        'at_self': MessageSegment.at(event.user_id),
        'rp': x
    }

    await rp.finish(Message.template(random.choice(s)).format_map(params))
