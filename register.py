from flask import Flask, render_template, request
import re

app = Flask(__name__)
@app.route("/regrep", methods=['GET', 'POST'])
def regrep():
    message = ""
    phone_number = ""

    if "phone_number" in request.form.keys():
        phone_number = request.form["phone_number"]

        if len(phone_number)==0 :
            message =  '携帯電話番号を入力してください。'
        elif re.match('^[0-9]{3}-[0-9]{4}-[0-9]{4}$', phone_number):
           message = 'あなたの携帯電話番号は「' + phone_number + '」です'
        else:
            message = '形式が違います。xxx-xxxx-xxxxの形式の数値で入力してください'

    return render_template('regrep.html', phone_number=phone_number, message=message)

@app.route("/register", methods=['GET','POST'])
def register():
    mail_adress = ""
    password = ""
    mail_message = ""
    pass_message = ""
    message = ""

    # mailadress,password の入力の確認後
    if "mail_adress" in request.form.keys():
        if "password" in request.form.keys(): 
            mail_adress = request.form.get("mail_adress")
            password = request.form.get("password")

            # mail_adress 判定
            if len(mail_adress) == 0: #未記入
                mail_message = 'アドレスが入力されていません。'
            elif re.match("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail_adress):
                mail_message = ''
            else: # 形式が違う場合
                mail_message = 'メールアドレスの形式が違います。'

            # password 判定
            if len(password) == 0: # passwordが未記入
                pass_message = "パスワードが入力されていません。"
            elif re.match(r'^[a-zA-Z0-9]{6,18}$',password):
                pass_message = ""
            else: # 形式が違う
                pass_message = "パスワードの形式が違います。"
            
            if re.match(r'^[0-9a-zA-Z]@[a-z]$', mail_adress) and re.match(r'^[a-zA-Z0-9]{6,18}$',password):
                message = "登録完了"

    return render_template("register.html", mail_adress=mail_adress, password=password, mail_message=mail_message, pass_message=pass_message, message=message)