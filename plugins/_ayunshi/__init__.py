from nonebot import on_command
from datetime import datetime
from nonebot.adapters.onebot.v11 import *
ys = on_command(".ys",block = True)

zf = ""

@ys.handle()
async def _(event: Event):
    date0 = datetime.today()
    yq = int(int(event.user_id)*date0.day%100)
    if(yq<=40):
        zf = ",虽然有运气不好的时候,但一切都会好起来的"
    if(yq>40 and yq<=60):
        zf = ",看来又是普通且安全的一天,至少不会突然暴毙"
    if(yq>60 and yq<=80):
        zf = ",今天会有好事发生~"
    if(yq>80 and yq<=100):
        zf = ",今天运气超级无敌好,冲!"
    await ys.finish(MessageSegment.at(event.user_id)+MessageSegment.text(f"今天的运气值为{yq}")+MessageSegment.text(f"{zf}"))