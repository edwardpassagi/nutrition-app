import sys
sys.path.insert(1, './')

import src.dao.processMealContainsDAO as processMealContainsDAO
import src.action.processMealAction as processMealAction
import src.action.processFoodAction as processFoodAction
import src.action.processPlanAction as processPlanAction

def removeFoodIdFromMealId(mid, fid):
    # remove food relationship from that meal
    processMealContainsDAO.removeFoodIdFromMealIdDAO(mid,fid)
    # TODO: remove foodCalories from mealCalories
    food = processFoodAction.getFoodById(fid)
    foodCalories = food[0]['food_calories']
    updateVal = "-" + str(foodCalories)
    processMealAction.updateMealCaloriesById(mid, updateVal)

    # TODO: remove foodCalories from planCalories that contains mealID
    processPlanAction.updatePlanCaloriesByMealId(mid, updateVal)

    return