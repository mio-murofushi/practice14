from flask import Flask, render_template
app = Flask(__name__)
@app.route("/send")
def send():
    return render_template('send.html')

from flask import request
@app.route("/receive", methods=["GET"])
def receive():
    if "my_name" in request.args.keys() :
        return "ここに入力した名前を表示： {}".format(request.args["my_name"])
    else:
        return "名前が未入力です"
