import sys
sys.path.insert(1, './')

import src.dao.processPlanDAO as processPlanDAO
import src.dao.processPlanContainsDAO as processPlanContainsDAO

def getAllPlans():
    plans = processPlanDAO.getAllPlansDAO()
    return plans

def deletePlanById(id):
    # delete plan instance
    processPlanDAO.deletePlanByIdDAO(id)
    # delete planID entry from the plan_contains table
    processPlanContainsDAO.deletePlanIdEntryDAO(id)
    return

def updatePlanCaloriesByMealId(mid, updateVal):
    # get all planIDs attached to mid
    planIDs = processPlanContainsDAO.getPlanIdsFromMealIdDAO(mid)

    # updateVal on all planCalories referred by pid
    for planID in planIDs:
        pid = planID['plan_id']
        processPlanDAO.updatePlanCaloriesByIdDAO(pid, updateVal)

    return