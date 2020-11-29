import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def addEmptyUser():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO user_info(user_id) values(NULL)"
        cursor.execute(cmd)
        conn.commit()
        user_id = getLastInsert()
        return user_id
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def getLastInsert():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cmd = "SELECT LAST_INSERT_ID()"
    cursor.execute(cmd)
    user_id = cursor.fetchall()
    return user_id

def editUserInfo(pid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM plan WHERE plan_id = {}".format(str(pid))
        cursor.execute(cmd)
        plans = cursor.fetchall()

        return plans
    
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def editUserHealthInfo(pid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM plan WHERE plan_id = {}".format(str(pid))
        cursor.execute(cmd)
        plans = cursor.fetchall()

        return plans
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def editUserNutrientDoses(pid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM plan WHERE plan_id = {}".format(str(pid))
        cursor.execute(cmd)
        plans = cursor.fetchall()

        return plans
    
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


