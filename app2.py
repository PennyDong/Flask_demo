from flask import Flask

# 建立Application 物件
app=Flask(__name__) 

#建立路徑 / 對應的處理函式

@app.route("/")
def index():
    return "您好歡迎參觀菜鳥工程師的作品"

@app.route("/data")
def handleData():
    return "My Data"

#動態路由:建立路由 /user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleUser(username):
    return "Hello "+username


app.run(port=3000)