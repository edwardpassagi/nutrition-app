import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def createNewFoodDAO(foodName, foodCalories, foodImage):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO food (food_name, food_image, food_calories) VALUES('{}', '{}', {});".format(foodName, foodImage, str(foodCalories))
        cursor.execute(cmd)
        conn.commit()

        # get the insertID
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT LAST_INSERT_ID();"
        cursor.execute(cmd)
        result = cursor.fetchall()
        # return the ID of the inserted meal
        return result[0]['LAST_INSERT_ID()']
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

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