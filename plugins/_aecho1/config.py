from nonebot import *
from nonebot.adapters.onebot.v11 import *

echo = on_command(".fd")
@echo.handle()
async def _(event:Event):
    message = event.get_message().extract_plain_text()
    message1 = ""

    for i in range(3,len(message)):
        message1+=message[i]
        
    await echo.finish(MessageSegment.text(message1))
