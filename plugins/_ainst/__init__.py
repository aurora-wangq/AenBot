from nonebot import *
from nonebot.adapters.onebot.v11 import *

inst = on_command("ahelp",block = True)

@inst.handle()
async def _():
    await inst.finish("用.ys使用今日运气功能\n直接发“爹”会回应“干嘛!”\n.fd内容,使用复读功能\n.bee 内容,使用最佳匹配搜索图片功能\n.sbee 内容-数量,来使用随机匹配指定数量相关内容图片\nahelp获取指令列表")
#用.ys使用今日运气功能\n直接发“爹”会回应“干嘛!”\n用.fd内容 使用复读功能\n使用.bee 内容,使用最佳匹配搜索图片功能\n使用.sbee 内容-数量,来使用随机匹配指定数量相关内容图片\n使用ahelp获取指令列表