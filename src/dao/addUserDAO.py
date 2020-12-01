import sys
from src.beans.UserBean import UserBean
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def addUser():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO user_info(user_id) values(NULL)"
        cursor.execute(cmd)
        conn.commit()
        user_id = getLastInsert(cursor)
        return user_id
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def getLastInsert(cursor):
    cmd = "SELECT LAST_INSERT_ID()"
    cursor.execute(cmd)
    sql_val = cursor.fetchall()
    user_id = sql_val[0]['LAST_INSERT_ID()']
    return user_id

def editUserInfo(user: UserBean):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "UPDATE user_info SET username='{}', first_name='{}', last_name='{}', hashed_password='{}', email='{}' WHERE user_id={}".format(user.getUsername(), user.getFirstName(), user.getLastName(), user.getPassword(), user.getEmail(), user.getUserID())
        cursor.execute(cmd)
        conn.commit()
        return
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()