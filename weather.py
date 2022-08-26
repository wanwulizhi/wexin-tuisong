import requests
import sys
import os
from lxml import etree
from time import time, localtime
# data = json.dumps({"userId": "aead7de17f814531ab5cba88a96bd932",
#                    "competitionId": "e50b219dabc3825583abdddb47980078",
#                    "score": 2550, "answerCount": 270,
#                    "answerRightCount": 255, "costTime": 0,
#                    "roomId": "c688b8202c3e4f89832f2ba5bb476d13"})
headers = {'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'keep-alive',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
           }


def postfuction(u, d):
    res = requests.post(u, d, headers=headers)
    return res.text


def getfuction(url, data):
    res = requests.get(url, data, headers=headers)
    return res.text


# def tip():
#     url = 'https://www.tianqi.com/taian1/life.html'

#     res = requests.get(url, headers=headers)
#     #拿到返回信息
#     restext=etree.HTML(res.text)
#     #转换为好处理的html格式
#     # try:
#     #     city_name=restext.xpath('//dd[@class="name"]/h2/text()')[0]
#     # except:
#     #     content='没有该城市信息哦，请注意查询格式不要调皮'
#     #     return content
#     city_temp=restext.xpath('//dl[@class="temp"]/dd[@class="txt"]/text()')
#     city_air=restext.xpath('//dl[@class="temp"]/dd[@class="air"]/text()')
#     city_life=restext.xpath('//ul[@class="lifeindex"]/a/li/b/text()')
#     for i in range(0,len(city_life)):
#         city_life[i]+=":"+restext.xpath('//ul[@class="lifeindex"]/a/li/b/em/text()')[i]
#         city_life[i]+=";"+restext.xpath('//ul[@class="lifeindex"]/a/li/p/text()')[i]
    
#     city_life.pop(1)
#     city_life.pop(3)
#     city_life.pop(4)
#     return str(city_life)
def get_weather():
    # 城市id
    try:
        city_id ="101120801"
    except KeyError:
        print("推送消息失败，请检查省份或城市是否正确")
        os.system("pause")
        sys.exit(1)
    # city_id = 101280101
    # 毫秒级时间戳
    t = (int(round(time() * 1000)))
    headers = {
        "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://d1.weather.com.cn/dingzhi/{}.html?_={}".format(city_id, t)
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    response_data = response.text.split(";")[0].split("=")[-1]
    response_json = eval(response_data)
    # print(response_json)
    weatherinfo = response_json["weatherinfo"]
    # 天气
    weather = weatherinfo["weather"]
    # 最高气温
    temp = weatherinfo["temp"]
    # 最低气温
    tempn = weatherinfo["tempn"]
    return weather, temp, tempn
def tip():
    
    url = "http://www.weather.com.cn/weather1d/101120801.shtml"
    res = requests.get(url, headers=headers)
    
    # retext=res.text.encode("ISO-8859-1").decode("utf-8")
    retext=res.content
    #拿到返回信息
    restext=etree.HTML(retext,parser=etree.HTMLParser(encoding='utf-8'))
    city_life=restext.xpath('//div[@class="livezs"]/ul/li/em/text()')
    clouths=str(restext.xpath('//div[@class="livezs"]/ul/li[@class="li3 hot"]/a/em/text()'))+":"+str(restext.xpath('//div[@class="livezs"]/ul/li[@class="li3 hot"]/a/span/text()'))+"---"+str(restext.xpath('//div[@class="livezs"]/ul/li[@class="li3 hot"]/a/p/text()'))
    #拼接穿衣指数
    for i in range(0,len(city_life)):
        city_life[i]+=":"+restext.xpath('//div[@class="livezs"]/ul/li/span/text()')[i]
        city_life[i]+="---"+restext.xpath('//div[@class="livezs"]/ul/li/p/text()')[i]
    #拼接其余指数
    city_life.append(clouths)
    return str(city_life).replace('[','').replace(']','').replace('\'','').replace('\"','')
print(tip())
