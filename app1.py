from flask import Flask, render_template
app = Flask(__name__)
@app.route('/users1')
def show_users():
    users1 = ["太郎","花子","一浪"]
    template_folder="templates"
    return render_template('users1.html',users=users1,template_folder='templates')