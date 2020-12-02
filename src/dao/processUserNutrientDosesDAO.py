
import sys
from typing import List
sys.path.insert(1, './')
import pymysql
from db_config import mysql
from src.enum.NutrientsEnum import NutrientNameEnum, NutrientWeightConstants
from src.beans.NutrientDoseBean import NutrientDoseBean
import src.dao.proccessNutrientDosesDAO as nutrientDosesDAO
from src.beans.UserBean import UserBean
from src.beans.userNutrientDoseBean import UserNutrientDoseBean
from datetime import date

def editUserNutrientDoses(user: UserBean):
    for value in NutrientNameEnum:
        nutrientDose: NutrientDoseBean = nutrientDosesDAO.getNutrient(value.value[1], date.today().year - user.getBirthYear(), user.getGender())
        addNutrientDose(nutrientDose, user)
        if value == NutrientNameEnum.CALORIES_CONSTANT:
            updateEnergyNutrient(user, nutrientDose)

def updateEnergyNutrient(user: UserBean, nutrientDose: NutrientDoseBean):
    if user.getUserDecision() == 'MAINTAIN':
        nutrientDose.setNutrientDoseIA(user.getDailyMaintainCalories())
        nutrientDose.setNutrientDoseUB(user.getDailyMaintainCalories() * NutrientWeightConstants.MAINTAIN_CALORIES_UB_CONSTANT.value)
        updateEnergyNutrientWeights(user, nutrientDose, NutrientWeightConstants.NUTRIENT_DEFAULT_WEIGHT.value, NutrientWeightConstants.NUTRIENT_DEFAULT_WEIGHT.value)
    elif user.getUserDecision() == 'LOSE':
        nutrientDose.setNutrientDoseIA(user.getDailyAdjustedCalories())
        nutrientDose.setNutrientDoseUB(user.getDailyAdjustedCalories() * NutrientWeightConstants.MAINTAIN_CALORIES_UB_CONSTANT.value)
        updateEnergyNutrientWeights(user, nutrientDose, NutrientWeightConstants.CALORIES_LBIA_WEIGHT.value, NutrientWeightConstants.NUTRIENT_DEFAULT_WEIGHT.value)
    elif user.getUserDecision() == 'GAIN':
        nutrientDose.setNutrientDoseIA(user.getDailyMaintainCalories())
        nutrientDose.setNutrientDoseUB(user.getDailyAdjustedCalories())
        updateEnergyNutrientWeights(user, nutrientDose, NutrientWeightConstants.NUTRIENT_DEFAULT_WEIGHT.value, NutrientWeightConstants.CALORIES_IAUB_WEIGHT.value)
    return

def updateEnergyNutrientWeights(user: UserBean, nutrientDose: NutrientDoseBean, weightBetweenLBandIA, weightBetweenIAandUB):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "UPDATE user_nutrient_doses SET IA={}, UB={}, weightBetweenLBandIA={}, weightBetweenIAandUB={} WHERE user_id={} AND nutrient_id={}".format(nutrientDose.getNutrientDoseIA(), nutrientDose.getNutrientDoseUB(), weightBetweenLBandIA, weightBetweenIAandUB, user.getUserID(), NutrientNameEnum.CALORIES_CONSTANT.value[1])
        cursor.execute(cmd)
        conn.commit()
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

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

def getUserNutrientDoses(user_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT nutrient_id, LB, IA, UB, weightLowerLB, default_scoreLowerLB, weightBetweenLBandIA, default_scoreBetweenLBandIA, weightBetweenIAandUB, default_scoreBetweenIAandUB FROM user_nutrient_doses WHERE user_id={}".format(user_id)
        cursor.execute(cmd)
        cursor_return = cursor.fetchall()
        return loadUserNutrientDosesInfo(user_id, cursor_return)
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()


def getUserNutrientDose(user_id, nutrient_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT nutrient_id, LB, IA, UB, weightLowerLB, default_scoreLowerLB, weightBetweenLBandIA, default_scoreBetweenLBandIA, weightBetweenIAandUB, default_scoreBetweenIAandUB FROM user_nutrient_doses WHERE user_id={} AND nutrient_id={}".format(user_id, nutrient_id)
        cursor.execute(cmd)
        cursor_return = cursor.fetchall()
        return loadUserNutrientInfo(user_id, cursor_return[0])
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def loadUserNutrientDosesInfo(user_id, useNutrientDosesDict):
    userNutrientsDosesList: List(UserNutrientDoseBean) = []
    for nutrientDoseInfo in useNutrientDosesDict:
        userNutrientsDosesList.append(loadUserNutrientInfo(user_id, nutrientDoseInfo))
    return userNutrientsDosesList


def loadUserNutrientInfo(user_id, userNutrientDoseDict):
    userNutrientDoseBean = UserNutrientDoseBean()
    userNutrientDoseBean.setNutrientDoseUserID(user_id)
    userNutrientDoseBean.setUserNutrientID(userNutrientDoseDict['nutrient_id'])
    userNutrientDoseBean.setUserNutrientLB(int(userNutrientDoseDict['LB']))
    userNutrientDoseBean.setUserNutrientIA(int(userNutrientDoseDict['IA']))
    userNutrientDoseBean.setUserNutrientUB(int(userNutrientDoseDict['UB']))
    userNutrientDoseBean.setUserNutreintWeightLowerLB(int(userNutrientDoseDict['weightLowerLB']))
    userNutrientDoseBean.setUserNutreintWeightBetweenLBandIA(int(userNutrientDoseDict['weightBetweenLBandIA']))
    userNutrientDoseBean.setUserNutreintWeightBetweenIAandUB(int(userNutrientDoseDict['weightBetweenIAandUB']))

    userNutrientDoseBean.setUserNutreintDefaultScoreLowerLB(int(userNutrientDoseDict['default_scoreLowerLB']))
    userNutrientDoseBean.setUserNutreintDefaultScoreBetweenLBandIA(int(userNutrientDoseDict['default_scoreBetweenLBandIA']))
    userNutrientDoseBean.setUserNutreintDefaultScoreBetweenIAandUB(int(userNutrientDoseDict['default_scoreBetweenIAandUB']))
    return userNutrientDoseBean
