from flask import Flask
from flask import request
from flask import render_template
from flask import session
app=Flask(
    __name__,
    static_folder="statec",
    static_url_path="/")


app.secret_key="password" #設定session的秘鑰

@app.route("/")
def index():
    return render_template("index_html")

@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"]=name #session["欄位名稱"=資料]
    return "您好"+name

@app.route("/talk")
def talk():
    name=session["username"]
    return "很高興見到您,彭彭"
 
app.run(port=3000)