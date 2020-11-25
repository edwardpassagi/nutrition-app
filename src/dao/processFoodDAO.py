import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def getFoodsByMealIdDAO(id):
    conn = None
    cursor = None
    try:
        # Get food
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        get_food_from_meal_cmd = "SELECT * FROM meal NATURAL JOIN meal_contains NATURAL JOIN food WHERE meal_id={};".format(str(id))
        cursor.execute(get_food_from_meal_cmd)
        foods = cursor.fetchall()
        return foods

    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def getFoodById(id):
    conn = None
    cursor = None
    try:
        # Get food
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM food WHERE food_id={};".format(str(id))
        cursor.execute(cmd)
        foods = cursor.fetchall()
        return foods

    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()