#http://cychengyuan-vod.48.cn/327574/20190330/cy/5c9e3df00cf2927bfdb8e112.m3u8
# 获取文件夹路径
# 保存的mp4文件名
import requests
import json
import os
import time

import asyncio
from ffmpeg import FFmpeg

member = '熊心瑶'

def getUrl():
    url2 = 'https://plive.48.cn/livesystem/api/live/v1/memberLivePage'
    lastUrl = ''
    headers={
        'version':'5.0.1',
        'os':'android',
        'Content-Type':'application/json;charset=utf-8'
    }

    d2 = {}
    resp = requests.post(url2,headers=headers,data=json.dumps(d2))
    print(resp.json())
    livearray = resp.json()['content']['liveList']
    for live in livearray:
        print(live['title'])
        print(live['streamPath'])
        if member in live['title']:
            if lastUrl != live['streamPath']:
                m3u8tomp4(live['streamPath'], member+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                lastUrl = live['streamPath']


def m3u8tomp4(url,name):
    os.system("ffmpeg -i %s -c copy /Users/minture/PycharmProjects/XXY/%s.flv" % url, name)

getUrl()



