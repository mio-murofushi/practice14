from flask import Flask, render_template, request
app = Flask(__name__)

# GETリクエストを受信
@app.route("/send", methods=["GET"])
def send():
    return render_template("prec2_send.html")

# POSTのリクエストを処理する関数
@app.route("/receave", methods=["POST"])
def receave():
    my_name = request.form.get("my_name")
    return render_template("prec2_receave.html",my_name=my_name)