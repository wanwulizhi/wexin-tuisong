import requests

from lxml import etree

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


def get_weather():
    url = 'https://www.tianqi.com/taian1/life.html'

    res = requests.get(url, headers=headers)
    #拿到返回信息
    restext=etree.HTML(res.text)
    #转换为好处理的html格式
    # try:
    #     city_name=restext.xpath('//dd[@class="name"]/h2/text()')[0]
    # except:
    #     content='没有该城市信息哦，请注意查询格式不要调皮'
    #     return content
    city_temp=restext.xpath('//dl[@class="temp"]/dd[@class="txt"]/text()')
    city_air=restext.xpath('//dl[@class="temp"]/dd[@class="air"]/text()')
    city_life=restext.xpath('//ul[@class="lifeindex"]/a/li/b/text()')
    for i in range(0,len(city_life)):
        city_life[i]+=":"+restext.xpath('//ul[@class="lifeindex"]/a/li/b/em/text()')[i]
        city_life[i]+=";"+restext.xpath('//ul[@class="lifeindex"]/a/li/p/text()')[i]
    return str(city_life)

print(get_weather())
