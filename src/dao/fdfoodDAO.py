from src.beans.FoodBean import FoodBean
from src.beans.userNutrientDoseBean import UserNutrientDoseBean
import src.dao.BrandedFoodDAO as brandedFoodDAO
import src.dao.FoodNutrientsDAO as foodNutrientsDAO
import sys
import pymysql
from db_config import mysql
sys.path.insert(1, './')


def getFoodByID(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT f.fdc_id, f.description, fn.amount FROM fdfood AS f JOIN food_nutrient AS fn ON fn.fdc_id = f.fdc_id JOIN nutrient AS n ON n.id = fn.nutrient_id JOIN branded_food AS bf ON bf.fdc_id = f.fdc_id WHERE f.fdc_id={}".format(id)
        cursor.execute(cmd)
        cursor_return = cursor.fetchall()[0]
        return loadFoodInfo(cursor_return)
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()
    


def getRandomFood(userNutrientDoseBean: UserNutrientDoseBean):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM (SELECT * FROM (SELECT * FROM (SELECT f.fdc_id, f.description, fn.amount FROM fdfood AS f JOIN food_nutrient AS fn ON fn.fdc_id = f.fdc_id JOIN nutrient AS n ON n.id = fn.nutrient_id JOIN branded_food AS bf ON bf.fdc_id = f.fdc_id WHERE n.id = {} AND f.data_type = \"branded_food\" AND (fn.amount <= {} AND fn.amount >= {}) ORDER BY fn.amount desc) AS t ORDER BY RAND() LIMIT 1000) AS t1 ORDER BY t1.amount desc) AS t2 ORDER BY RAND() LIMIT 1".format(userNutrientDoseBean.getUserNutrientID(), userNutrientDoseBean.getUserNutrientUB(), userNutrientDoseBean.getUserNutrientLB())
        cursor.execute(cmd)
        cursor_return = cursor.fetchall()[0]
        return loadFoodInfo(cursor_return)
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def loadFoodInfo(foodDict):
    fdfoodBean = FoodBean()
    foodInfo = brandedFoodDAO.getFoodInfo(foodDict['fdc_id'])
    foodNutrientsInfo = foodNutrientsDAO.getFoodNutrientsInfo(foodDict['fdc_id'])
    fdfoodBean.setBrandedFoodFdcID(foodDict['fdc_id'])
    fdfoodBean.setBrandedFoodDescription(foodDict['description'])
    fdfoodBean.setBrandedFoodBrandOwner(foodInfo['brand_owner'])
    fdfoodBean.setBrandedFoodIngredients(foodInfo['ingredients'])
    fdfoodBean.setBrandedFoodServingSize(foodInfo['serving_size'])
    fdfoodBean.setBrandedFoodServingSizeUnit(foodInfo['serving_size_unit'])
    fdfoodBean.setBrandedFoodHouseholdServingFulltext(foodInfo['household_serving_fulltext'])
    fdfoodBean.setBrandedFoodCategoryDesc(foodInfo['branded_food_category'])
    fdfoodBean.setBrandedFoodNutrientsAmounts(foodNutrientsInfo)
    return fdfoodBean
