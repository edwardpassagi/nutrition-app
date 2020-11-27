import sys
sys.path.insert(1, './')

import src.action.processPlanAction as processPlanAction

import src.dao.processMealDAO as processMealDAO
import src.dao.processMealContainsDAO as processMealContainsDAO
import src.dao.processPlanContainsDAO as processPlanContainsDAO

def createNewMeal(mealName, mealCalories = 0):
    mid = processMealDAO.createNewMealDAO(mealName, mealCalories)
    return mid

def getMealByMealId(id):
    meal = processMealDAO.getMealByMealIdDAO(id)
    return meal

def getMealsByPlanID(id):
    meals = processMealDAO.getMealsByPlanIdDAO(id)
    return meals

def removeMealByID(pid, mid):
    # TODO: subtract plan calories from the mealCalories
    meal = getMealByMealId(mid)
    mealCalories = meal[0]['meal_calories']
    print("MEAL CALORIES: {}".format(mealCalories))
    updateVal = "-" + str(mealCalories)

    processPlanAction.updatePlanCaloriesByPlanId(pid, updateVal)
    processMealDAO.removeMealByIdDAO(mid)
    processMealContainsDAO.removeMealIdFromMealContains(mid)
    processPlanContainsDAO.removeMealIdFromPlanContains(mid)
    return

def updateMealCaloriesById(id, updateVal):
    processMealDAO.updateMealCaloriesByIdDAO(id, updateVal)
    return