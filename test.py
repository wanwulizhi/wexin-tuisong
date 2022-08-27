from requests import get, post
from datetime import datetime, date
import sys
import os
from datetime import datetime, date
from time import time, localtime

    # appId
# app_id = "wx13a18f62749951b0"
#     # appSecret
# app_secret = "d970fb29f201da25337a0f93e261ff7e"
# post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(app_id, app_secret))
# res=get(post_url)
# try:
#     access_token = res.json()['access_token']
# except KeyError:
#     print(res.text)
#     os.system("pause")
#     sys.exit(1)
# # print(access_token)
# print(access_token)
# access_token='60_Q-TvGrvW-W0EMwR35Wqbi31TAovLMErmcaqZhV-djswAmHS7QxTNJ4H2FKrHT2P4gFDkpWCrfvLWI-pOLYLncd--ujwvEydg_td6bRoZDEo6kAKTMRASyhplzCbIRIUYSL9MkhdiqlZl7nbjNOLeAJATUR'
# url="https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token="+access_token
# res=get(url)
year = localtime().tm_year
month = localtime().tm_mon
day = localtime().tm_mday
we_date="2022-9-13"
today = datetime.date(datetime(year=year, month=month, day=day))
we_year = int(we_date.split("-")[0])
we_month = int(we_date.split("-")[1])
we_day = int(we_date.split("-")[2])
we_date = date(we_year, we_month, we_day)
# 获取在一起的日期差
we_days = str(we_date.__sub__(today)).split(" ")[0]
result=we_days.replace('-','')
print(result)