from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import *
from nonebot.adapters.onebot.v11.helpers import MessageSegment
from nonebot.adapters.onebot.v11.event import *
from nonebot.adapters.onebot.v11.bot import Bot

echo = on_command(".fd")

@echo.handle()
async def _(arg: Message = CommandArg()):
    await echo.finish(MessageSegment.text(arg.extract_plain_text()))
