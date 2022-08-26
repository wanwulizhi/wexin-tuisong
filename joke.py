import requests
import json

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


def get_joke():
    url = 'https://www.neihantv.cn/wp-admin/admin-ajax.php'
    data= {"action":"ajax_more_posts",
                      "start":"0",
                      "catid":"1"}
    res = requests.post(url, data, headers=headers)
    #拿到返回信息
    # print(res.text.encode('utf-8').decode('unicode_escape'))
    restext=json.loads(res.text)
    #转换为好处理的json格式
    jokes=[]
    for i in range(0,len(restext)):
        jokes.append(restext[i]['title'])
    return jokes

print(get_joke())
