from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__,static_folder="static",static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page")
def page():
    return render_template("page.html")

@app.route("/show")
def show():
    name=request.args.get("n", "")
    return "歡迎來到 "+name+"個人網頁"


#使用POST連線
@app.route("/Total", methods=["POST"])
def Total():
    maxNumber=request.form["max"]
    maxNumber=int(maxNumber)
    result=0
    for n in range(1,maxNumber):
        result+=n
    return render_template("result.html",data=result)

app.run(port=3000)