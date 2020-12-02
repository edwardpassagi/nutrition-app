import sys
sys.path.insert(1, './')

import src.dao.processFoodDAO as processFoodDAO

def createNewFood(foodName, foodCalories, username, foodImage = ""):
    fid = processFoodDAO.createNewFoodDAO(foodName, foodCalories, foodImage, username)
    return fid

def getFoodsByMealID(id):
    foods = processFoodDAO.getFoodsByMealIdDAO(id)
    return foods

def getFoodById(id):
    food = processFoodDAO.getFoodById(id)
    return food

def getFoodByKeyword(foodKeyword, username):
    foods = processFoodDAO.getFoodByKeywordDAO(foodKeyword, username)
    return foods