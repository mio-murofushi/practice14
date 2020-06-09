from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/get_sample")
def get_sample():
    return render_template('get_sample.html', query=request.args.get("query"))