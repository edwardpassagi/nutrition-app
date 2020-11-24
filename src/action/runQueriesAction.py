import pymysql
from db_config import mysql
import sys
sys.path.insert(1, './src/dao/')
from runQueriesDAO import executeFileCommands

CREATE_TABLE_FILE = "./SQL/CreateAllTables.sql"
DROP_TABLE_FILE = "./SQL/dropAllTables.sql"

FOOD_TABLE_INSERT_FILE_PATH = "./SQL/food.sql"
MEAL_CONTAINS_TABLE_INSERT_FILE_PATH = "./SQL/meal_contains.sql"
MEAL_TABLE_INSERT_FILE_PATH = "./SQL/meal.sql"
PLAN_CONTAINS_TABLE_INSERT_FILE_PATH = "./SQL/plan_contains.sql"
PLAN_TABLE_INSERT_FILE_PATH = "./SQL/plan.sql"

FILE_PATHS = [FOOD_TABLE_INSERT_FILE_PATH, MEAL_CONTAINS_TABLE_INSERT_FILE_PATH, MEAL_TABLE_INSERT_FILE_PATH, PLAN_CONTAINS_TABLE_INSERT_FILE_PATH,
                PLAN_TABLE_INSERT_FILE_PATH]

def dropAllTables():
    drop_tables_file = open(DROP_TABLE_FILE, 'r')
    executeFileCommands(drop_tables_file)
    drop_tables_file.close()

def createAllTables():
    create_tables_file = open(CREATE_TABLE_FILE, 'r')
    executeFileCommands(create_tables_file)
    create_tables_file.close()

def execute_files():
    for file_path in FILE_PATHS:
        commands_file = open(file_path, 'r')
        executeFileCommands(commands_file)
        commands_file.close()

def execute_sql_folder():
    dropAllTables()
    createAllTables()
    execute_files()