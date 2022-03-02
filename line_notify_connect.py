import requests

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