import sys
import pymysql
from db_config import mysql
sys.path.insert(1, './')




def getFoodInfo(fdc_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT brand_owner, ingredients, serving_size, serving_size_unit, household_serving_fulltext, branded_food_category FROM branded_food WHERE fdc_id={}".format(fdc_id)
        cursor.execute(cmd)
        return cursor.fetchall()[0]
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()