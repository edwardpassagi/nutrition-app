import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def linkPidToMidDAO(pid,mid):
    conn = None
    cursor = None
    try:
        # add PID and MID to plan_contains entry
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO plan_contains (plan_id, meal_id) VALUES({},{});".format(str(pid), str(mid))
        cursor.execute(cmd)
        conn.commit()

        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

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

def getMealIdsFromPlanIdDAO(pid):
    conn = None
    cursor = None
    try:
        # Delete fid from mid
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "SELECT meal_id FROM plan_contains WHERE plan_id={};".format(str(pid))
        print(cmd)
        cursor.execute(cmd)
        mealIDs = cursor.fetchall()
        return mealIDs
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()