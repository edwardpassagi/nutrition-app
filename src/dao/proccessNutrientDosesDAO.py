from src.beans.NutrientDoseBean import NutrientDoseBean
import sys
from typing import Dict
sys.path.insert(1, './')
import pymysql
from db_config import mysql


def getNutrient(nutrient_id, age, gender):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT LB, IA, UB FROM nutrient_doses WHERE max_age >= {} AND (gender = '{}' OR gender = 'IDC') AND nutrient_id = {} ORDER BY max_age ASC LIMIT 1;".format(age, gender, nutrient_id)
        cursor.execute(cmd)
        cursor_return = cursor.fetchall()
        return processData(cursor_return, nutrient_id)
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def processData(cursor_return, nutrient_id):
    nutrientBean = NutrientDoseBean()
    nutrientBean.setNutrientID(nutrient_id)
    nutrientBean.setNutrientDoseLB(cursor_return[0]['LB'])
    nutrientBean.setNutrientDoseIA(cursor_return[0]['IA'])
    nutrientBean.setNutrientDoseUB(cursor_return[0]['UB'])
    return nutrientBean

