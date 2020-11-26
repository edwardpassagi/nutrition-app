import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def createNewPlanDAO(planName, planCalories):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO plan (plan_name, plan_calories) VALUES ('{}',{})".format(planName, str(planCalories))
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def getAllPlansDAO():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM plan")
        plans = cursor.fetchall()

        return plans
    
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