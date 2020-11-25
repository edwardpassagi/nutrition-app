import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def getMealsByPlanIdDAO(id):
    conn = None
    cursor = None
    try:
        # Get meals
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        get_meal_from_plan_cmd = "SELECT meal_id, meal_name, meal_calories FROM plan NATURAL JOIN plan_contains pc NATURAL JOIN meal m where plan_id = {};".format(str(id))
        cursor.execute(get_meal_from_plan_cmd)
        meals = cursor.fetchall()

        return meals
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def removeMealByIdDAO(id):
    conn = None
    cursor = None
    try:
        # Remove meal by its id
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "DELETE FROM meal WHERE meal_id={};".format(str(id))
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()
    
def updateMealCaloriesByIdDAO(id, updateVal):
    """updateVal is formatted like "+100" or "-100"
    """
    conn = None
    cursor = None
    try:
        # Remove meal by its id
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "UPDATE meal SET meal_calories = meal_calories {} WHERE meal_id = {}".format(updateVal ,str(id))
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()