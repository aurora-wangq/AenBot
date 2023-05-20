from nonebot import *
from nonebot.adapters.onebot.v11 import *
import time
import requests
import json
import urllib
from nonebot.params import CommandArg
import random
from nonebot.adapters.onebot.v11.helpers import Cooldown

img = on_command(".bee",block = True)

@img.handle(parameterless = [Cooldown(cooldown=20, prompt='没完没了了是吧')])
async def _(arg: Message = CommandArg()):
   global word
   word = arg.extract_plain_text()

   header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
   page = 2
   pn = 0
   url_ = ""
   for i in range(1,page):
        url = 'https://image.baidu.com/search/acjson?'
    
        param = {
            'tn': 'resultjson_com',
            'logid': '',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'fr': '',
            'word': word,   #图片类型
            'queryWord': word,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z':'' ,
            'ic':'0' ,
            'hd': '',
            'latest': '',
            'copyright': '',
            's':'' ,
            'se':'' ,
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'expermode': '',
            'nojc': '',
            'isAsync': '',
            'pn': pn,#从第几张图片开始
            'rn': '1',
            'gsm': '',
        }
    
        jpgs=requests.get(url=url,headers=header,params=param)
        jpg=json.loads(jpgs.text)
        jpg=jpg['data']
        
        del jpg[-1]
        for jd in jpg:
            url_ += jd['thumbURL']
   await img.send(MessageSegment.image(url_))
