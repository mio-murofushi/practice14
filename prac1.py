from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/sample1", methods=["GET"])
def send(gender="",my_name="",mail=""):
    return render_template('sample1.html', gender=gender, my_name=my_name,mail=mail)

@app.route("/sample1", methods=["POST"])
def sample():
    my_name = request.form.get("my_name","")
    gender = request.form.get("gender","")
    mail = request.form.get("mail","")
    return send(my_name, gender, mail)