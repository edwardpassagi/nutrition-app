import sys
sys.path.insert(1, './')

import src.action.removeMealAction as removeMealAction

import src.dao.processPlanDAO as processPlanDAO
import src.action.processPlanContainsAction as processPlanContainsAction

def deletePlanIdEntry(pid):
    # set pid planCalories to 0
    # processPlanDAO.setPlanCaloriesFromPlanIdDAO(pid, 0)
    # delete mid entries from pid
    mids = processPlanContainsAction.getMealIdsFromPid(pid)
    for mid in mids:
        removeMealAction.removeMealByID(pid,mid)
    # Delete pid from planContains
    # processPlanContainsDAO.deletePlanIdEntryDAO(pid)
    return