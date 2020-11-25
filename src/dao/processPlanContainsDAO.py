import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def deletePlanIdEntryDAO(id):
    conn = None
    cursor = None
    try:
        # Delete by planID
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "DELETE FROM plan_contains WHERE plan_id={};".format(str(id))
        cursor.execute(cmd)
        conn.commit()

        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def removeMealIdFromPlanContains(mid):
    conn = None
    cursor = None
    try:
        # Delete fid from mid
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "DELETE FROM plan_contains WHERE meal_id={};".format(str(mid))
        print(cmd)
        cursor.execute(cmd)
        conn.commit()

        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def getPlanIdsFromMealIdDAO(mid):
    conn = None
    cursor = None
    try:
        # Delete fid from mid
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT plan_id FROM plan_contains WHERE meal_id={};".format(str(mid))
        print(cmd)
        cursor.execute(cmd)
        planIDs = cursor.fetchall()
        return planIDs
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()