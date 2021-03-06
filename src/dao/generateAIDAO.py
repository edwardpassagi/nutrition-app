import sys
sys.path.insert(1, './')

import pymysql
from db_config import mysql

def createNewPlanSQL(planName, planCalories, username):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO plan (plan_name, plan_calories, username) VALUES('{}', {}, '{}');".format(planName, str(planCalories), username)
        # print(cmd)
        cursor.execute(cmd)
        conn.commit()

        # get the insertID
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT LAST_INSERT_ID();"
        # print(cmd)
        cursor.execute(cmd)
        result = cursor.fetchall()
        # print(result)
        return result[0]['LAST_INSERT_ID()']
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


def linkFoodIdToMealId(mealID, foodID):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO meal_contains (meal_id, food_id) VALUES({}, {});".format(str(mealID), str(foodID))
        # print(cmd)
        cursor.execute(cmd)
        conn.commit()

    except Exception as e:
        print(e)
        return 0
    
    finally:
        cursor.close()
        conn.close()

def linkMealIDtoPlanID(planID, mealID):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO plan_contains (plan_id, meal_id) VALUES({}, {});".format(str(planID), str(mealID))
        # print(cmd)
        cursor.execute(cmd)
        conn.commit()

    except Exception as e:
        print(e)
        return 0
    
    finally:
        cursor.close()
        conn.close()