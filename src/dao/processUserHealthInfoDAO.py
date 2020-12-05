import sys
import pymysql
from db_config import mysql
sys.path.insert(1, './')
from src.beans.UserBean import UserBean

def editUserHealthInfo(user: UserBean):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO user_health_info VALUES({}, '{}', {}, '{}', {}, {}, {}, {}, '{}', {}, {}, {}, {}, {}, {})".format(user.getUserID(), user.getGender(), user.getBirthYear(), user.getUserDecision(), user.getWeight(), user.getTargetWeight(), user.getTargetTimeFrame(), user.getHeight(), user.getDailyActivity(), user.getIsPregnant(), user.getIsNursing(), user.getBMI(), user.getBMR(), user.getDailyMaintainCalories(), user.getDailyAdjustedCalories())
        cursor.execute(cmd)
        conn.commit()
        return
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def getUserHealthInfo(user_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT * FROM user_health_info WHERE user_id={}".format(user_id)
        cursor.execute(cmd)
        cursor_return = cursor.fetchall()
        return loadUserHealthInfo(user_id, cursor_return[0])
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def loadUserHealthInfo(user_id, userHealthInfoDict):
    userBean = UserBean();
    userBean.setUserID(user_id)
    userBean.setGender(userHealthInfoDict['gender'])
    userBean.setBirthYear(userHealthInfoDict['birthYear'])
    userBean.setUserDecision(userHealthInfoDict['user_decision'])
    userBean.setWeight(userHealthInfoDict['weight'])
    userBean.setTargetWeight(userHealthInfoDict['target_weight'])
    userBean.setTargetTimeFrame(userHealthInfoDict['target_timeframe'])
    userBean.setHeight(userHealthInfoDict['height_inches'])
    userBean.setDailyActivity(userHealthInfoDict['daily_activity'])
    userBean.setIsPregnant(userHealthInfoDict['is_pregnant'])
    userBean.setIsNursing(userHealthInfoDict['is_nursing'])
    userBean.setBMI(userHealthInfoDict['BMI'])
    userBean.setBMR(userHealthInfoDict['BMR'])
    userBean.setDailyMaintainCalories(userHealthInfoDict['daily_maintain_calories'])
    userBean.setDailyAdjustedCalories(userHealthInfoDict['daily_adjusted_calories'])
    return userBean


