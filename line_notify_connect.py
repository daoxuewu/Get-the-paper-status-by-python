import requests
#如果 terminal 訊息顯示尚未安裝 requests模組 ，請在 terminal 終端機輸入以下指令 pip install requests ，安裝完後就可以順利執行了

# 定義連接 Line notify 的函式
#reference : https://notify-bot.line.me/doc/en/
def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

##打包用 auto-py-to-exe 附加文件出問題解決方法
##reference:
## 官方文件:https://nitratine.net/blog/post/issues-when-using-auto-py-to-exe/?utm_source=auto_py_to_exe&utm_medium=application_link&utm_campaign=auto_py_to_exe_help&utm_content=top
## stackoverflow:https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
## 簡體中文教學:https://zhuanlan.zhihu.com/p/130328237
# def resource_path(relative_path):
#     """獲取程序中所需文件資源的絕對路徑"""
#     try:
#         # PyInstaller創建臨時文件夾，將路徑儲存於_MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)


# if __name__ == "__main__":
#   token = 'line notify的權證'
#   message = '基本功能測試'
#   lineNotifyMessage(token, message)

