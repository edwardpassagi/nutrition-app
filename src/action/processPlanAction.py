import sys
sys.path.insert(1, './')

import src.action.processPlanContainsAction as processPlanContainsAction
import src.dao.processPlanDAO as processPlanDAO
import src.dao.processPlanContainsDAO as processPlanContainsDAO

def createNewPlan(planName, planCalories = 0):
    processPlanDAO.createNewPlanDAO(planName,planCalories)
    return

def getAllPlans():
    plans = processPlanDAO.getAllPlansDAO()
    return plans

def getPlanById(pid):
    plan = processPlanDAO.getPlanByIdDAO(pid)
    return plan

def deletePlanById(id):
    # delete plan instance
    processPlanDAO.deletePlanByIdDAO(id)
    # delete planID entry from the plan_contains table
    processPlanContainsDAO.deletePlanIdEntryDAO(id)
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
