import sys
sys.path.insert(1, './')

import src.neo.dao.processUserDAO as processUserDAO

def createNewUserNode(username):
    processUserDAO.createNewUserNodeDAO(username)
    return

def isValidUsername(username):
    """Returns True if username exists in neo4j
    """
    isValidUser = processUserDAO.isValidUsername(username)
    return isValidUser

def getUserFollowings(username):
    following_names = processUserDAO.getUserFollowingsDAO(username)
    return following_names

def getUserFollowers(username):
    follower_names = processUserDAO.getUserFollowersDAO(username)
    return follower_names

def getNonFollowedUsers(username):
    nonfollowed_names = processUserDAO.getNonFollowedUsersDAO(username)
    return nonfollowed_names

def followUser(username, toFollowUsername):
    processUserDAO.followUserDAO(username, toFollowUsername)
    return

def unfollowUser(username, toUnfollowUsername):
    processUserDAO.unfollowUserDAO(username, toUnfollowUsername)
    return
