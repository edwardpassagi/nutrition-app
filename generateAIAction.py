import pymysql
from db_config import mysql

def createNewMealSQL(mealName, mealCalories):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO meal (meal_name, meal_calories) VALUES('{}', {});".format(mealName, str(mealCalories))
        print(cmd)
        cursor.execute(cmd)
        conn.commit()

        # get the insertID
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT LAST_INSERT_ID();"
        print(cmd)
        cursor.execute(cmd)
        result = cursor.fetchall()
        print(result)
        return result[0]['LAST_INSERT_ID()']
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def createNewPlanSQL(planName, planCalories):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO plan (plan_name, plan_calories) VALUES('{}', {});".format(planName, str(planCalories))
        print(cmd)
        cursor.execute(cmd)
        conn.commit()

        # get the insertID
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT LAST_INSERT_ID();"
        print(cmd)
        cursor.execute(cmd)
        result = cursor.fetchall()
        print(result)
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
        print(cmd)
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
        print(cmd)
        cursor.execute(cmd)
        conn.commit()

    except Exception as e:
        print(e)
        return 0
    
    finally:
        cursor.close()
        conn.close()