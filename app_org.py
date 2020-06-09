from flask import Flask, render_template
app = Flask(__name__)

"""
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello") #URLを指定
def hello():
    return "Hello, World!"

@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return "User {}".format(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return "Post {}".format(post_id)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return "Subpath {}".format(subpath)
"""
@app.route('/users1')
def show_users():
    users = ["太郎", "花子", "一浪"]
    return render_template('users1.html', users=users)