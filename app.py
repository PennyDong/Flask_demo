from flask import Flask

app=Flask(__name__) #__name__ 代表目前執行的模組

@app.route("/") #函式的裝飾(Decorator): 以函式為基礎，並提供附加功能
def home():
    return "Hello Flask"

@app.route("/test")
def test():
    return "Test Flask"

if __name__=="__main__": #如果以主程式執行


    app.run(port=3000) #啟動伺服器,可透過prot 參數指定阜號