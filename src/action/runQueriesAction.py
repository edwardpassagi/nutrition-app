import os
import sys
sys.path.insert(1, './')
from src.dao.runQueriesDAO import executeFileCommands
from src.beans.UserBean import *
from src.action.addUserAction import *

CREATE_TABLE_FILE = "SQL/CreateAllTables.sql"
DROP_TABLE_FILE = "SQL/dropAllTables.sql"
ABSOLUTE_PATH = 'SQL/mysql/'

FILE_PATHS = os.listdir(ABSOLUTE_PATH)

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
        if file_path.endswith(".sql"):
            commands_file = open(ABSOLUTE_PATH+file_path, 'r')
            executeFileCommands(commands_file)
            commands_file.close()


def createUserTest1():
    userTest1 = UserBean()
    userTest1.setUsername("hhache2")
    userTest1.setFirstName("sam")
    userTest1.setLastName("hachem")
    userTest1.setPassword("qwertyuio")
    userTest1.setEmail("hhache2@illinois.edu")
    userTest1.setGender("M")
    userTest1.setBirthYear(1999)
    userTest1.setUserDecision("MAINTAIN")
    userTest1.setWeight(150)
    userTest1.setTargetWeight(130)
    userTest1.setTargetTimeFrame(12)
    userTest1.setHeight(71)
    userTest1.setDailyActivity("MODERATE")
    userTest1.setIsPregnant(False)
    userTest1.setIsNursing(False)
    addNewUser(userTest1)

def createUserTest2():
    userTest1 = UserBean()
    userTest1.setUsername("tonov2")
    userTest1.setFirstName("simon")
    userTest1.setLastName("tonov")
    userTest1.setPassword("qwe3rty4")
    userTest1.setEmail("simon@tonov.edu")
    userTest1.setGender("M")
    userTest1.setBirthYear(2005)
    userTest1.setUserDecision("LOSE")
    userTest1.setWeight(220)
    userTest1.setTargetWeight(180)
    userTest1.setTargetTimeFrame(10)
    userTest1.setHeight(72)
    userTest1.setDailyActivity("HARD")
    userTest1.setIsPregnant(False)
    userTest1.setIsNursing(False)
    addNewUser(userTest1)

def createUserTest3():
    userTest1 = UserBean()
    userTest1.setUsername("passagi2")
    userTest1.setFirstName("edward")
    userTest1.setLastName("passagi")
    userTest1.setPassword("qwe5rty5")
    userTest1.setEmail("edward@passagi.edu")
    userTest1.setGender("M")
    userTest1.setBirthYear(1960)
    userTest1.setUserDecision("LOSE")
    userTest1.setWeight(300)
    userTest1.setTargetWeight(220)
    userTest1.setTargetTimeFrame(15)
    userTest1.setHeight(68)
    userTest1.setDailyActivity("LIGHT")
    userTest1.setIsPregnant(False)
    userTest1.setIsNursing(False)
    addNewUser(userTest1)

def createUserTest4():
    userTest1 = UserBean()
    userTest1.setUsername("mcroberts")
    userTest1.setFirstName("paige")
    userTest1.setLastName("mcroberts")
    userTest1.setPassword("qwe5rty5")
    userTest1.setEmail("paige@mcroberts.edu")
    userTest1.setGender("F")
    userTest1.setBirthYear(1999)
    userTest1.setUserDecision("GAIN")
    userTest1.setWeight(150)
    userTest1.setTargetWeight(170)
    userTest1.setTargetTimeFrame(12)
    userTest1.setHeight(71)
    userTest1.setDailyActivity("HARD")
    userTest1.setIsPregnant(False)
    userTest1.setIsNursing(False)
    addNewUser(userTest1)

def createUserTest5():
    userTest1 = UserBean()
    userTest1.setUsername("mccarthy2")
    userTest1.setFirstName("evelynn")
    userTest1.setLastName("underwood")
    userTest1.setPassword("qwe5rty5")
    userTest1.setEmail("evelynn@underwood.edu")
    userTest1.setGender("F")
    userTest1.setBirthYear(1970)
    userTest1.setUserDecision("LOSE")
    userTest1.setWeight(210)
    userTest1.setTargetWeight(160)
    userTest1.setTargetTimeFrame(10)
    userTest1.setHeight(75)
    userTest1.setDailyActivity("MODERATE")
    userTest1.setIsPregnant(False)
    userTest1.setIsNursing(False)
    addNewUser(userTest1)

def runCreateUserTests():
    createUserTest1()
    createUserTest2()
    createUserTest3()
    createUserTest4()
    createUserTest5()

def ProcessAllSQLFiles():
    dropAllTables()
    createAllTables()
    execute_files()
    runCreateUserTests()