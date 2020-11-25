import os
import sys
sys.path.insert(1, './')
from src.dao.runQueriesDAO import executeFileCommands

CREATE_TABLE_FILE = "SQL/CreateAllTables.sql"
DROP_TABLE_FILE = "SQL/dropAllTables.sql"
ABSOLUTE_PATH = 'SQL/mysql/'

FILE_PATHS = os.listdir('SQL/mysql/')

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
        commands_file = open(ABSOLUTE_PATH+file_path, 'r')
        executeFileCommands(commands_file)
        commands_file.close()

def ProcessAllSQLFiles():
    dropAllTables()
    createAllTables()
    execute_files()