import nonebot
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent

def check_(event: PokeNotifyEvent):
    return event.target_id == event.self_id

work = on_notice(rule=check_)

friend_ = [940136983,1659304852,2018411135,2083412529]

@work.handle()
async def _(event: PokeNotifyEvent):
    if(event.user_id in friend_):
        await work.finish("喵~")
    else:
        await work.finish("别戳我行吗")
    
    
