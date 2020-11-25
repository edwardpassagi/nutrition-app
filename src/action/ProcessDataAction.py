import sys
sys.path.insert(1, './')
import os
from src.action.runQueriesAction import ProcessAllSQLFiles
from src.action.ProcessCSVFilesAction import processAllCSVFiles


def processDataIntoDatabase():
    ProcessAllSQLFiles()
    processAllCSVFiles()