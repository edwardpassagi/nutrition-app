import sys
sys.path.insert(1, './')

import src.action.processPlanContainsAction as processPlanContainsAction
import src.dao.processMealDAO as processMealDAO
import src.dao.processPlanDAO as processPlanDAO
import src.dao.processPlanContainsDAO as processPlanContainsDAO
import src.dao.processMealContainsDAO as processMealContainsDAO

def createNewPlan(planName, planCalories = 0):
    processPlanDAO.createNewPlanDAO(planName,planCalories)
    return

def getAllPlans():
    plans = processPlanDAO.getAllPlansDAO()
    return plans

def getPlanById(pid):
    plan = processPlanDAO.getPlanByIdDAO(pid)
    return plan

def deletePlanById(pid):
    # get all meal IDs associated with it
    mids = processPlanContainsAction.getMealIdsFromPid(pid)
    # delete all meal IDs entrance and its associated meal_contains
    for mid in mids:
        processMealDAO.removeMealByIdDAO(mid)
        processMealContainsDAO.removeMealIdFromMealContains(mid)

    # delete plan instance
    processPlanDAO.deletePlanByIdDAO(pid)
    # delete planID entry from the plan_contains table
    processPlanContainsDAO.deletePlanIdEntryDAO(pid)
    return

def updatePlanCaloriesByMealId(mid, updateVal):
    # get all planIDs attached to mid
    planIDs = processPlanContainsAction.getPlanIdsFromMealId(mid)
    # updateVal on all planCalories referred by pid
    for planID in planIDs:
        updatePlanCaloriesByPlanId(planID, updateVal)
    return

def updatePlanCaloriesByPlanId(pid, updateVal = "+0"):
    processPlanDAO.updatePlanCaloriesByPlanIdDAO(pid, updateVal)
    return

def setPlanCaloriesFromPlanId(pid, planCalories = 0):
    processPlanDAO.setPlanCaloriesFromPlanIdDAO(pid, planCalories)
    return
