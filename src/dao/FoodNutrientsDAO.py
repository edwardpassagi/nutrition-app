from src.beans.NutrientBean import NutrientBean
import src.enum.NutrientsEnum as nutrientEnums
import sys
from typing import List
import pymysql
from db_config import mysql
sys.path.insert(1, './')


def getFoodNutrientsInfo(fdc_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT fn.nutrient_id, n.name, n.unit_name, fn.amount FROM food_nutrient AS fn JOIN nutrient AS n ON fn.nutrient_id = n.id WHERE fdc_id ={} and fn.nutrient_id in (1087, 1091, 1090, 1092, 1093, 1089, 1101, 1098, 1095, 1104, 1162, 1109, 1185, 1165, 1167, 1170, 1008)".format(fdc_id)
        cursor.execute(cmd)
        return loadFoodNutrientsInfo(cursor.fetchall())
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()


def loadFoodNutrientsInfo(nutrientsAmountsInfo):
    nutrientsList: List(NutrientBean) = []
    for element in nutrientEnums.NutrientNameEnum:
        nutrient = NutrientBean()
        nutrient.setNutrientID(element.value[1])
        nutrient.setNutrientName(element.value[0])
        nutrientsList.append(nutrient)

    for nutrientInfoDict in nutrientsAmountsInfo:
        for nutrient in nutrientsList:
            if(nutrientInfoDict['nutrient_id'] == nutrient.getNutrientID()):
                nutrient.setNutrientUnitName(nutrientInfoDict['unit_name'])
                nutrient.setNutrientAmount(nutrientInfoDict['amount'])
    return nutrientsList
    