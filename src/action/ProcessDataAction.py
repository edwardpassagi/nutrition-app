import sys
sys.path.insert(1, './')
import os
from src.action.runQueriesAction import ProcessAllSQLFiles


def processDataIntoDatabase():
    ProcessAllSQLFiles()