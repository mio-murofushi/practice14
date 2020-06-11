#coding:UTF-8
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, request

app = Flask(__name__)

host = 'localhost' # データベースのホスト名又はIPアドレス
username = 'root'  # MySQLのユーザ名
passwd   = 'Mimu1997'    # MySQLのパスワード
dbname   = 'my_database'    # データベース名

# 第12章Sample1
@app.route("/mysql_select")
def mysql_select():
    # DB接続
    # 返り値：MySQLConnection(サーバへの接続を表すオブジェクト)
    
    goods = []
    
    try:
        # データベースの情報を渡し、接続
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        
        # クエリ実行
        cursor = cnx.cursor()
        query = 'SELECT good_id, goods_name, price FROM goods_table' #実行するクエリ
        cursor.execute(query)

        # 実行したクエリ結果の取得
        for (id, name, price) in cursor:
            item = {"good_id":id, "goods_name":name, "price":price}
            goods.append(item)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:

        # DB切断
        cnx.close()

    return render_template("goods.html", goods = goods)

# 第12章sample2
@app.route("/mysql_sample")
def mysql_sample():
    order = ""
    if "order" in request.args.keys() :
            order = request.args.get("order")

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        
        query = 'SELECT goods_name, price FROM goods_table ORDER BY price ' + order
        cursor.execute(query)
        goods = []
        for (name, price) in cursor:
            item = {"name": name, "price":price}
            goods.append(item)
        params = {
        "asc_check" : order == "ASC",
        "desc_check" : order == "DESC",
        "goods" : goods
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

    return render_template("goods.html", **params)

@app.route("/mysql_change")
def mysql_change():
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        #query = "INSERT INTO goods_table(good_id, goods_name, price) VALUES(5,'サイダー', 100)"
        #query = "UPDATE goods_table SET price = 60 WHERE good_id = 5"
        query = "DELETE FROM goods_table WHERE good_id = 6"
        # クエリの実行
        cursor.execute(query)
        cnx.commit() # この処理が無いと変更が反映されません！

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return "終了"

# 第１２章　課題１
@app.route("/emp_sample")
def challenge_mysql_select():
    jobs = ""
    if "jobs" in request.args.keys():
        jobs = request.args.get("jobs")

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        if jobs == "":
            query = "SELECT * FROM emp_table"
        else:
            query = f"SELECT * FROM emp_table WHERE job = '{jobs}'"
        
        cursor.execute(query)
        emp = []
    
        for (id, name, job, age) in cursor:
            item = {"emp_id":id, "emp_name":name, "job":job, "age":age}
            emp.append(item)
        
        params={
            "all" : jobs == "",
            "manager" : jobs == "manager",
            "analyst" : jobs == "analyst",
            "clerk" : jobs == "clerk",
            "emp" : emp
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
    
    return render_template("emp.html", **params)