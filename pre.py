from flask import Flask,render_template
app = Flask(__name__)
@app.route('/users1')

def show_users():
    users1 = ["太郎","花子","一浪"]
    return render_template('user1.html',users=users1)