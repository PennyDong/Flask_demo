from flask import Flask
from flask import request

app=Flask(__name__,
          static_folder="static",
          static_url_path="/") #__name__ 代表目前執行的模組

@app.route("/") #函式的裝飾(Decorator): 以函式為基礎，並提供附加功能
def index():
    print("請求方法",request.method)
    print("通訊協定",request.scheme)
    print("主機名稱",request.host)
    print("路徑",request.path)
    print("完整的網址",request.url)
    print("-----------------")
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好",request.headers.get("accept-language"))
    print("引薦網址",request.headers.get("referrer"))

    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "您好，Flask"

@app.route("/test")
def test():
    return "Test Flask"

if __name__=="__main__": #如果以主程式執行


    app.run(port=3000) #啟動伺服器,可透過prot 參數指定阜號