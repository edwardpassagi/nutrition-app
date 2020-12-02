import sys
sys.path.insert(1, './')
import csv
import pymysql
from db_config import mysql

def createNewMealDAO(cmd):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(cmd)
        conn.commit()
        return
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


def fill_food_data():
    cmd = "INSERT INTO food (food_name, food_calories) VALUES "
    with open("food-cal.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # i = 0
        for row in reader:
            food = ""
            for i in range(len(row)-1):
                food += row[i]
            calories = row[len(row)-1]

            curFoodStr = "( '{}', {} ),".format(food,calories)
            cmd += curFoodStr
            # i += 1
        cmd = cmd[:-1]
        cmd += ';'
        createNewMealDAO(cmd)


if __name__ == "__main__":
    fill_food_data()