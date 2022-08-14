import os

USER_ID = 'USER_ID'
APP_ID =  'APP_ID'
APP_SECRET = 'APP_SECRET'
TEMPLATE_ID = 'TEMPLATE_ID'
START_DATE = 'START_DATE'
BIRTHDAY = 'START_DATE'
CITY = 'CITY'
PROVICE = 'PROVICE'
# 公众号配置
# 公众号appId

# app_id = "wx0268dabce1770b63"
app_id = os.environ(APP_ID)
# 公众号appSecret
# app_secret = "e82c0bb576888426b1118dc17613d150"
app_secret = os.environ(APP_SECRET)
# 模板消息id
# template_id = "q6bkfgm-YLnULGEnRNB_EH985YQpkMtFS0TZ81CLnVc"

template_id = os.environ(TEMPLATE_ID)
# 接收公众号消息的微信号

# hanke
user = "oGhoI6nm1IEfcOCr74fK15ZRs6tw"
if USER_ID in os.environ:
    user = os.environ[USER_ID]

# 徐
# user = "oGhoI6jAa_zqGi1G_ztZRuWXm5AE"


# 信息配置
# 所在省份
province = os.environ[PROVICE]
# 所在城市
city = os.environ[CITY]
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1
birthday = os.environ[BIRTHDAY]
# 在一起的日子，格式同上
love_date = os.environ[START_DATE]

