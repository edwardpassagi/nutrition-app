import pymysql
from db_config import mysql
import pandas as pd

def executeRow(command):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(command)
        conn.commit()
    except Exception as e:
        print("An error occured: {}".format(e))
    finally:
        cursor.close()
        conn.close()

def loadFoodCategoryFile(data):
    for row in data.itertuples():
        executeRow(row)
        