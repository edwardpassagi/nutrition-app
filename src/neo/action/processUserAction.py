import sys
sys.path.insert(1, './')

import src.neo.dao.processUserDAO as processUserDAO

def createNewUserNode(username):
    processUserDAO.createNewUserNodeDAO(username)
    return

def isValidUsername(username):
    """Returns True if username exists in neo4j
    """
    return processUserDAO.isValidUsername(username)
