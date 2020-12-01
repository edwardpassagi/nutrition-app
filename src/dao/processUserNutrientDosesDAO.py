import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql
from src.enum.NutrientsEnum import NutrientNameEnum
from src.beans.NutrientDoseBean import NutrientDoseBean
import src.dao.proccessNutrientDosesDAO as nutrientDosesDAO
from src.beans.UserBean import UserBean
from datetime import date

def editUserNutrientDoses(user: UserBean):
    for value in NutrientNameEnum:
        nutrientDose: NutrientDoseBean = nutrientDosesDAO.getNutrient(value.value[1], date.today().year - user.getBirthYear(), user.getGender())
        addNutrientDose(nutrientDose, user)

def addNutrientDose(nutrientDose: NutrientDoseBean, user: UserBean):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO user_nutrient_doses(user_id, nutrient_id, LB, IA, UB) VALUES({}, {}, {}, {}, {})".format(user.getUserID(), nutrientDose.getNutrientID(), nutrientDose.getNutrientDoseLB(), nutrientDose.getNutrientDoseIA(), nutrientDose.getNutrientDoseUB())
        cursor.execute(cmd)
        conn.commit()
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()