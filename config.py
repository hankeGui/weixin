# coding=UTF-8
import os

USER_ID = 'USER_ID'
USER_ID_HANKE = 'USER_ID_HANKE'
USER_ID_XU = 'USER_ID_XU'
APP_ID = 'APP_ID'
APP_SECRET = 'APP_SECRET'
TEMPLATE_ID = 'TEMPLATE_ID'
START_DATE = 'START_DATE'
BIRTHDAY = 'START_DATE'
CITY = 'CITY'
PROVINCE = 'PROVINCE'
TEST = 'TEST'
# 公众号配置
# 公众号appId

# app_id = "wxa3a95bb8a11d26f6"
app_id = "wxa3a95bb8a11d26f6"
if APP_ID in os.environ:
    app_id = os.environ[APP_ID]
# 公众号appSecret
# app_secret = "cabbb2c0d5d3b8093096877b10d50b60"
app_secret = "cabbb2c0d5d3b8093096877b10d50b60"
if APP_SECRET in os.environ:
    app_secret = os.environ[APP_SECRET]
# 模板消息id
# template_id = "q6bkfgm-YLnULGEnRNB_EH985YQpkMtFS0TZ81CLnVc"

template_id = "q6bkfgm-YLnULGEnRNB_EH985YQpkMtFS0TZ81CLnVc"
if TEMPLATE_ID in os.environ:
    template_id = os.environ[TEMPLATE_ID]
# 接收公众号消息的微信号

# hanke oGhoI6nm1IEfcOCr74fK15ZRs6tw
userList = []
if USER_ID in os.environ:
    userList.append(os.environ[USER_ID])
if USER_ID_XU in os.environ:
    userList.append(os.environ[USER_ID_XU])
if USER_ID_HANKE in os.environ:
    userList.append(os.environ[USER_ID_HANKE])


# 徐
# user = "oGhoI6jAa_zqGi1G_ztZRuWXm5AE"


# 信息配置
# 所在省份
province = "陕西"
if PROVINCE in os.environ:
    province = os.environ[PROVINCE]
# 所在城市
city = "西安"
if CITY in os.environ:
    city = os.environ[CITY]
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1
birthday = "1996-2-2"
if BIRTHDAY in os.environ:
    birthday = os.environ[BIRTHDAY]
# 在一起的日子，格式同上
love_date = "2022-8-10"
if START_DATE in os.environ:
    love_date = os.environ[START_DATE]

test_push = ""
if TEST in os.environ:
    test_push = os.environ[TEST]

