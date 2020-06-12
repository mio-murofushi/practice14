# 13章ひとこと掲示板作成

#coding:UTF-8
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, request

app = Flask(__name__)

host = 'localhost' # データベースのホスト名又はIPアドレス
username = 'root'  # MySQLのユーザ名
passwd   = 'Mimu1997'    # MySQLのパスワード
dbname   = 'my_database'    # データベース名

@app.route("/board")
def board_sample():
    add_username = "" # 20文字以内ユザネ
    add_comment = "" # 100文字以内コメント
    mes = ""

    # ユザネ、コメントの取得
    if "add_username" in request.args.keys(): 
        add_username = request.args.get("add_username")   
    if "add_comment" in request.args.keys():
        add_comment = request.args.get("add_comment")
    
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        
        # 新規クエリが存在した場合
        if add_username == "" and add_comment =="":
            print("入力情報がありません")

        elif len(add_username) > 20 or len(add_comment) > 100:
            print("name-error or comment-error")
            mes = "名前は２０文字以内、コメントは１００文字以内で！"
                
        elif add_username == "" or add_comment == "":
            print("Only name or comment")
            mes = "名前とコメントの両方をコメントしてください！"
        
        else:
            query =  f"INSERT INTO board_table(username, comment) VALUES('{add_username}', '{add_comment}')"
            # クエリの実行
            cursor.execute(query)
            cnx.commit()
            print("投稿完了！")
            mes = "投稿完了！"
            add_username = ""
            add_comment = ""

        query = 'SELECT username, comment, date FROM board_table'
        cursor.execute(query)

        user_data = []
        for (name, comment, date) in cursor:
            item = {"username": name, "comment":comment, "date":date}
            user_data.append(item)

        params = {
        "user_data" : user_data,
        "mes" : mes
        }

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("board.html", **params)
