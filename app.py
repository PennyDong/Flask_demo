from flask import Flask
from flask import request

app=Flask(__name__,
          static_folder="static",
          static_url_path="/") #__name__ 代表目前執行的模組

#建立路徑 /getSum 對應的處理函式
#利用要求字串 (Query String)提供彈性 例:getSum?max=最大數字
@app.route("/getSum")
def getSum():
    maxNumber=request.args.get("max",100) #預設值為100
    maxNumber=int(maxNumber)
    #在終端機裡顯示輸入的最大數字
    print("最大數字",maxNumber)
    result=0
    for n in range(1,maxNumber+1):
        result+=n
    return "結果:"+str(result)

@app.route("/getNumber")
def getNumber():
    maxNumber=request.args.get("max",1000)
    maxNumber=int(maxNumber)
    minNumber=request.args.get("min",10)
    minNumber=int(minNumber)
    print("最小值:",minNumber,"最大值:",maxNumber)
    result=0
    for n in range(minNumber,maxNumber+1):
        result+=n
    return "結果:"+str(result)    

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