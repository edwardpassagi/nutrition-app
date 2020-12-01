import py2neo

import pymysql
from db_config import mysql
from app import app

@app.route('/')
def mysql_test():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM user_data"
        cursor.execute(cmd)
        data = cursor.fetchall()
        print(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()