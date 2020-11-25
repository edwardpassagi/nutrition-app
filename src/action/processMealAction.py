import sys
sys.path.insert(1, './')

import src.dao.processMealDAO as processMealDAO
import src.dao.processMealContainsDAO as processMealContainsDAO
import src.dao.processPlanContainsDAO as processPlanContainsDAO

def getMealsByPlanID(id):
    meals = processMealDAO.getMealsByPlanIdDAO(id)
    return meals

def removeMealByID(id):
    processMealDAO.removeMealByIdDAO(id)
    processMealContainsDAO.removeMealIdFromMealContains(id)
    processPlanContainsDAO.removeMealIdFromPlanContains(id)
    return

def updateMealCaloriesById(id, updateVal):
    processMealDAO.updateMealCaloriesByIdDAO(id, updateVal)
    return