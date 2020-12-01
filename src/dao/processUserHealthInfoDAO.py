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


