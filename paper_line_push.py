from ser_easy import paper_status
from line_notify_connect import lineNotifyMessage

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
token = config.get('line-notify', 'notify_token') #在config.ini修改成你的line notify token
whatplace = str(config.get('line-notify', 'whatplace'))
p = whatplace + "印表機紙捲狀態:"

if paper_status == "12":
    message = p + '紙捲狀態正常'
    lineNotifyMessage(token, message)
elif paper_status == "1e":
    message = p + '下方探測器缺紙'
    lineNotifyMessage(token, message)
elif paper_status == "72":
    message = p + '上方探測器缺紙'
    lineNotifyMessage(token, message)
elif paper_status == "7e":
    message = p + '上下都沒紙了'
    lineNotifyMessage(token, message)
else:
    message="其他未設定狀態:"+str(paper_status)