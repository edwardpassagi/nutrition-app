import pymysql
from db_config import mysql

def executeCommand(command):
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

def executeFileCommands(file):
    content = ''
    try:
        content = file.read()
    except Exception as e:
        print("An error occured: {}".format(e))
    commands = content.split(';')
    commands.pop()
    for command in commands:
        executeCommand(command)
