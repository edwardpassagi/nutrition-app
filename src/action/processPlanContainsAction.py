import sys
sys.path.insert(1, './')

import src.dao.processPlanContainsDAO as processPlanContainsDAO

def linkPidToMid(pid,mid):
    processPlanContainsDAO.linkPidToMidDAO(pid,mid)
    return
