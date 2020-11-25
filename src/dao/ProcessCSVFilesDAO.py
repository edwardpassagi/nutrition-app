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

def loadFoodCategoryFile(file_name, data):
    for row in data.itertuples():
        # not a final implementation of a csv. this assumes we only have 3 columns. 
        # it does not have to be implemented.
        execution_string = '''INSERT INTO ?(?, ?, ?) VALUES(?, ?, ?)'''
        executeRow(execution_string)
        