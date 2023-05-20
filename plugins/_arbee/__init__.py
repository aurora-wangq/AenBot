from nonebot import *
from nonebot.adapters.onebot.v11 import *
import time
import requests
import json
import urllib
from nonebot.params import CommandArg
import random
from nonebot.adapters.onebot.v11.helpers import Cooldown

img = on_command(".sbee",block = True)

@img.handle(parameterless = [Cooldown(cooldown=20, prompt='没完没了了是吧')])
async def _(arg: Message = CommandArg()):
   global word
   word1 = arg.extract_plain_text()
   list_ = word1.split("-")
   word = list_[0]
   header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
   page = int(list_[1])+1
   pn = random.randint(0,(page-1)*30-1)
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
            'rn': int(list_[1]),
            'gsm': '',
        }
        global url_
        url_ = []
        jpgs=requests.get(url=url,headers=header,params=param)
        jpg=json.loads(jpgs.text)
        jpg=jpg['data']
        del jpg[-1]
        url_ += jpg
   for jd in url_:
    await img.send(MessageSegment.image(jd['thumbURL']))
