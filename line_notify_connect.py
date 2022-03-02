import requests
#如果 terminal 訊息顯示尚未安裝 requests模組 ，請在 terminal 終端機輸入以下指令 pip install requests ，安裝完後就可以順利執行了

# 定義連接 Line notify 的函式
def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


# if __name__ == "__main__":
#   token = 'line notify的權證'
#   message = '基本功能測試'
#   lineNotifyMessage(token, message)

#reference : https://notify-bot.line.me/doc/en/