from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent
from nonebot.rule import to_me

word=on_command("爹",block=True)

@word.handle()
async def _(event: GroupMessageEvent):
    await word.finish(Message(f"[CQ:at,qq={event.user_id}]干嘛!"))