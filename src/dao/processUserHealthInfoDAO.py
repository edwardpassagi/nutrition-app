import sys
sys.path.insert(1, './')
import src.beans.UserBean as userBean

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


