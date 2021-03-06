import sys
sys.path.insert(1, './')

import src.dao.processPlanContainsDAO as processPlanContainsDAO

def linkPidToMid(pid,mid):
    processPlanContainsDAO.linkPidToMidDAO(pid,mid)
    return

def getMealIdsFromPid(pid):
    meals = processPlanContainsDAO.getMealIdsFromPlanIdDAO(pid)
    mealIDs = []
    for meal in meals:
        mealID = meal['meal_id']
        mealIDs.append(mealID)
    return mealIDs

def getPlanIdsFromMealId(mid):
    plans = processPlanContainsDAO.getPlanIdsFromMealIdDAO(mid)
    planIDs = []
    for plan in plans:
        planID = plan['plan_id']
        planIDs.append(planID)
    return planIDs