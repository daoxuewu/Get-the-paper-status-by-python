from ser_easy import paper_status
from line_notify_connect import lineNotifyMessage

import configparser #配置文件解析器
import datetime     #時間模組

#增加實時當地時間
now = datetime.datetime.now()
timeString = "\n偵測時間 : " + str(now.strftime("%Y/%m/%d %H:%M:%S"))#Python time strftime()函數用於格式化時間

#讀取config設定檔內的值
config = configparser.ConfigParser()
#打包成exe檔後放工作排程器執行時若出現 configparser.nosectionerror 錯誤，解決方法是read改成讀絕對路徑
config.read('config.ini',encoding="utf-8-sig") # encoding="utf-8-sig" 可以解決windows因為BOM(byte order mark位元組標記)讀取中文時顯示亂碼的問題
# config.read((resource_path('config.ini')),encoding="utf-8-sig") # resource_path方法 用 auto-py-to-exe 把專案打包成一個exe檔，附加文件出問題解決方法附加文件出問題解決方法
token = config.get('default', 'notify_token') # 在config.ini修改成你的line notify token
whatplace = str(config.get('default', 'whatplace'))

p = "\n" + whatplace + "\n印表機狀態 : "

if paper_status == "12":
    message = p + '紙捲狀態正常' + timeString
    lineNotifyMessage(token, message)
elif paper_status == "1e":
    message = p + '下方探測器缺紙' + timeString
    lineNotifyMessage(token, message)
elif paper_status == "72":
    message = p + '上方探測器缺紙' + timeString
    lineNotifyMessage(token, message)
elif paper_status == "7e":
    message = p + '上下都沒紙了' + timeString
    lineNotifyMessage(token, message)
else:
    message="其他未設定狀態:"+str(paper_status) + timeString