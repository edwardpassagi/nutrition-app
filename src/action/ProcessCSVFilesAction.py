import sys
import pandas as pd
import os
sys.path.insert(1, './')
from src.dao.ProcessCSVFilesDAO import loadFoodCategoryFile

FILE_PATHS = os.listdir('CSV/')

FOOD_CATEGORY_FILE_PATH = r'CSV/food_category.csv'

def processFoodCategoryFileData():
    foodCategoryDataFile = pd.read_csv(FOOD_CATEGORY_FILE_PATH)
    df = pd.DataFrame(foodCategoryDataFile, columns=['id', 'code', 'description'])
    return df

def processAllCSVFiles():
    foodCategoryData = processFoodCategoryFileData()
    # print(foodCategoryData)
    # loadFoodCategoryFile(foodCategoryData)

