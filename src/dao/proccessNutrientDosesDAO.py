import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql


def getNutrient(pid):
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