from requests import get, post
from datetime import datetime, date
import sys
import os

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
access_token='60_Q-TvGrvW-W0EMwR35Wqbi31TAovLMErmcaqZhV-djswAmHS7QxTNJ4H2FKrHT2P4gFDkpWCrfvLWI-pOLYLncd--ujwvEydg_td6bRoZDEo6kAKTMRASyhplzCbIRIUYSL9MkhdiqlZl7nbjNOLeAJATUR'
url="https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token="+access_token
res=get(url)