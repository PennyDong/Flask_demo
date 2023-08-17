from flask import Flask

# 建立Application 物件,可以設定靜態檔案的路徑
app=Flask(
    __name__,
    #"靜態檔案的資料夾名稱"
    static_folder="static", 
    #"靜態檔案的網址路徑" 
    static_url_path="/"  
) 

#所有在static資料夾底下的檔案，都對應到網址路徑/更改的資料夾名稱(也可以改成"/")/檔案名稱

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