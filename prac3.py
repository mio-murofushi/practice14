from flask import Flask, render_template, request
import random

app = Flask(__name__)

# GETリクエストを受信
@app.route("/result", methods=["GET"])
def send():
    return render_template("prec3.html")

# POSTリクエストの送信
@app.route("/result",methods=["POST"])
def jyanken():
    # じゃんけんの選択を取得
    jyanken = request.form.get("jyanken", "")
    
    # 相手のじゃんけん選択をランダムに取得
    list=("グー","チョキ","パー")
    opp = random.choice(list)

    # じゃんけんの勝敗
    if jyanken == "グー":
        if  opp == "チョキ":
            result = "勝ち！"
        else:
            result = "負け"

    elif jyanken == "チョキ":
        if  opp == "パー":
            result = "勝ち！"
        else:
            result = "負け"

    elif jyanken  == "パー":
        if  opp == "グー":
            result = "勝ち！"
        else:
            result = "負け"
    else:
        result = "負け"
    return render_template("prec3.html",jyanken=jyanken, opp=opp, result=result)