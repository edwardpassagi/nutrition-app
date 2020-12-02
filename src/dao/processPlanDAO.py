import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def createNewPlanDAO(planName, username, planCalories):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO plan (plan_name, plan_calories, username) VALUES ('{}',{},'{}')".format(planName, str(planCalories), username)
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def getPlanByIdDAO(pid):
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

def getAllPlansDAO(username):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM plan WHERE username='{}'".format(username))
        plans = cursor.fetchall()

        return plans
    
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def setPlanCaloriesFromPlanIdDAO(pid, planCalories):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cmd = "UPDATE plan SET plan_calories = {} WHERE plan_id = {}".format(planCalories, pid)
        cursor.execute(cmd)
        conn.commit()
        return 
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def deletePlanByIdDAO(id):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM plan WHERE plan_id=%s", (id,))
        conn.commit()
        return 
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def updatePlanCaloriesByPlanIdDAO(id, updateVal):
    """updateVal is formatted like "+100" or "-100"
    """
    conn = None
    cursor = None
    try:
        # Remove meal by its id
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "UPDATE plan SET plan_calories = plan_calories {} WHERE plan_id = {}".format(updateVal ,str(id))
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def renamePlanByPidDAO(pid, newPlanName):
    conn = None
    cursor = None
    try:
        # update plan name
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "UPDATE plan SET plan_name = '{}' WHERE plan_id = {}".format(newPlanName ,str(pid))
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()