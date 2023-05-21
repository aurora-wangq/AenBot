import requests
import json


class BaiduImageAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'

    def search(self, text, **args):
        params = {
            'tn': 'resultjson_com',
            'logid': '',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'fr': '',
            'word': text,  # 图片类型
            'queryWord': text,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            's': '',
            'se': '',
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
            'pn': '0',
            'rn': '30',
            'gsm': '',
        }
        params.update(args)

        res = self.session.get('https://image.baidu.com/search/acjson?', params=params)
        data = json.loads(res.text)

        return [i for i in data['data'] if i]
