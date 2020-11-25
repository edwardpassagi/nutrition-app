import sys
import pandas as pd
import os
sys.path.insert(1, './')
from src.dao.ProcessCSVFilesDAO import loadFoodCategoryFile

DIRECTORY_PATH = 'CSV/'
FILE_PATHS = os.listdir(DIRECTORY_PATH)

def processCVSFileData(file_name):
    foodCategoryDataFile = pd.read_csv(file_name)
    # this assumes the food category csv file. 
    # does not need to be implemented.
    df = pd.DataFrame(foodCategoryDataFile, columns=['id', 'code', 'description'])
    return df

def processAllCSVFiles():
    for file_name in FILE_PATHS:
        if file_name.endswith('.csv'):  
            foodCategoryData = processCVSFileData(file_name)
            loadFoodCategoryFile(file_name, foodCategoryData)

