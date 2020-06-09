from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/post_sample", methods=["GET"])
def sample(gender=""):
    return render_template('post_sample.html', gender=gender)
 
@app.route("/post_sample", methods=["POST"])
def post_sample():
    gender = request.form.get("gender","")
    return sample(gender)
