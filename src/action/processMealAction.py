import sys
sys.path.insert(1, './')


import src.dao.processMealDAO as processMealDAO

def createNewMeal(mealName, mealCalories = 0):
    mid = processMealDAO.createNewMealDAO(mealName, mealCalories)
    return mid

def getMealByMealId(id):
    meal = processMealDAO.getMealByMealIdDAO(id)
    return meal

def getMealsByPlanID(id):
    meals = processMealDAO.getMealsByPlanIdDAO(id)
    return meals

def updateMealCaloriesById(id, updateVal):
    processMealDAO.updateMealCaloriesByIdDAO(id, updateVal)
    return

def renameMealByMid(mid, newMealName):
    processMealDAO.renameMealByMidDAO(mid, newMealName)
    return