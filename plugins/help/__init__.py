from nonebot import get_driver, on_command, get_loaded_plugins
from nonebot.adapters import Message
from nonebot.params import *
from nonebot.adapters.onebot.v11.helpers import MessageSegment
from nonebot.adapters.onebot.v11.event import *
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin import PluginMetadata

from .config import Config
from .utils import *

global_config = get_driver().config
config = Config.parse_obj(global_config)

__plugin_meta__ = PluginMetadata(
    name="Help",
    description="",
    usage=""".help [plugin] 显示帮助，若未指定plugin则显示所有可用的帮助""",
    config=Config
)

help = on_command("help", priority=1, block=True)


@help.handle()
async def help_main(bot: Bot, event: Event, arg: Message = CommandArg()):
    plugins = get_loaded_plugins()
    res = []
    s = arg.extract_plain_text()
    if s:
        suc = 0
        for i in plugins:
            if i.metadata:
                if i.metadata.name == s:
                    suc = 1
                    await help.finish(i.metadata.usage)
        if not suc:
            await help.finish(f"[ERROR] Plugin {s} not found")
    else:
        for i in plugins:
            if i.metadata:
                s = ""
                if i.metadata.name:
                    s += "Plugin: " + i.metadata.name + '\n'
                if i.metadata.usage:
                    s += "Usage: \n" + i.metadata.usage + '\n'
                res.append(MessageSegment.text(s))
        await send_forward_msg(bot, event, res)
