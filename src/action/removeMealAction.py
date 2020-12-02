import sys
sys.path.insert(1, './')

import src.action.processPlanAction as processPlanAction
import src.action.processMealAction as processMealAction

import src.dao.processMealDAO as processMealDAO
import src.dao.processMealContainsDAO as processMealContainsDAO
import src.dao.processPlanContainsDAO as processPlanContainsDAO



def removeMealByID(pid, mid):
    meal = processMealAction.getMealByMealId(mid)
    mealCalories = meal[0]['meal_calories']
    # print("MEAL CALORIES: {}".format(mealCalories))
    updateVal = "-" + str(mealCalories)

    processPlanAction.updatePlanCaloriesByPlanId(pid, updateVal)
    processMealDAO.removeMealByIdDAO(mid)
    processMealContainsDAO.removeMealIdFromMealContains(mid)
    processPlanContainsDAO.removeMealIdFromPlanContains(mid)
    return