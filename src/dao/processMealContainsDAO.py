import sys
sys.path.insert(1, './')
import pymysql
from db_config import mysql

def linkMidToFidDAO(mid,fid):
    conn = None
    cursor = None
    try:
        # add MID and FID to meal_contains entry
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "INSERT INTO meal_contains (meal_id, food_id) VALUES({},{});".format(str(mid), str(fid))
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


def unlinkMidToFidDAO(mid,fid):
    conn = None
    cursor = None
    try:
        # Delete fid from mid
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "DELETE FROM meal_contains WHERE meal_id={} AND food_id={} LIMIT 1;".format(str(mid), str(fid))
        # print(cmd)
        cursor.execute(cmd)
        conn.commit()

        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

def removeMealIdFromMealContains(mid):
    conn = None
    cursor = None
    try:
        # Delete fid from mid
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cmd = "DELETE FROM meal_contains WHERE meal_id={};".format(str(mid))
        # print(cmd)
        cursor.execute(cmd)
        conn.commit()

        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

        