from line_notify_connect import lineNotifyMessage

import serial #pyserial

import configparser #配置文件解析器
import datetime     #時間模組

#讀取config設定檔內的值
config = configparser.ConfigParser()
#打包成exe檔後放工作排程器執行時若出現 configparser.nosectionerror 錯誤，解決方法是read改成讀絕對路徑
config.read('config.ini',encoding="utf-8-sig") # encoding="utf-8-sig" 可以解決windows因為BOM(byte order mark位元組標記)讀取中文時顯示亂碼的問題
# config.read((resource_path('config.ini')),encoding="utf-8-sig") # resource_path方法 用 auto-py-to-exe 把專案打包成一個exe檔，附加文件出問題解決方法附加文件出問題解決方法
token = config.get('default', 'notify_token') # 在config.ini修改成你的line notify token
whatplace = str(config.get('default', 'whatplace'))
port = config.get('default', 'port') # 在config.ini修改成你的port

# 開啟串列埠(Serial port)，並得到串列埠物件 
serialPort = serial.Serial(
    port="COM2",
    baudrate=115200,
    bytesize=8,
    parity="N", 
    stopbits=1,
    timeout=1.00)

#寫入16進制資料
ans = serialPort.write(b'\x10\x04\x04')
#十六進位制的讀取
paper_status = serialPort.read().hex()

#準備打印在line上面的訊息
printerinfo = "\n" + whatplace + "\n印表機狀態 : "
#增加實時當地時間
now = datetime.datetime.now()
timeString = "\n偵測時間 : " + str(now.strftime("%Y/%m/%d %H:%M:%S"))#Python time strftime()函數用於格式化時間

#印表機回傳hex轉成line訊息
if paper_status == "12":
    message = printerinfo + '紙捲狀態正常' + timeString
    lineNotifyMessage(token, message)
elif paper_status == "1e":
    message = printerinfo + '下方探測器缺紙' + timeString
    lineNotifyMessage(token, message)
elif paper_status == "72":
    message = printerinfo + '上方探測器缺紙' + timeString
    lineNotifyMessage(token, message)
elif paper_status == "7e":
    message = printerinfo + '上下都沒紙了' + timeString
    lineNotifyMessage(token, message)
else:
    message="其他未設定狀態:"+str(paper_status) + timeString

#關閉串列埠
serialPort.close()
