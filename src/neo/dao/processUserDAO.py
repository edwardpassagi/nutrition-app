import sys
sys.path.insert(1, './')

from db_config import neo

def createNewUserNodeDAO(username):
    query = """
    MERGE (n:User{name:$username}) return n.name as name
    """
    formatter = {"username": username}
    neo.run(query, formatter)
    return

def isValidUsername(username):
    query = """
    MATCH (c:User{name:$curUser})
    return c
    """

    formatter = {"curUser": username}
    results = neo.run(query, formatter)

    # User exists if result is not null
    for result in results:
        if result:
            return True

    return False

def getUserFollowingsDAO(username):
    query = """
    MATCH (c:User{name:$username})-[r:FOLLOWS]->(f:User)
    return f.name as name
    """

    formatter = {"username": username}
    results = neo.run(query, formatter)

    following_names = []
    for result in results:
        following_names.append(result["name"])
    
    return following_names

def getUserFollowersDAO(username):
    query = """
    MATCH (c:User{name:$username})<-[r:FOLLOWS]-(f:User)
    return f.name as name
    """

    formatter = {"username": username}
    results = neo.run(query, formatter)

    follower_names = []
    for result in results:
        follower_names.append(result["name"])
    
    return follower_names

def getNonFollowedUsersDAO(username):
    query = """
    MATCH (current_user:User{name:$username}), (other_users:User)
    WHERE NOT (current_user)-[:FOLLOWS]->(other_users) and current_user<>other_users
    RETURN other_users.name as name
    """

    formatter = {"username": username}
    results = neo.run(query, formatter)

    nonfollowed_names = []
    for result in results:
        nonfollowed_names.append(result["name"])
    
    return nonfollowed_names

def followUserDAO(username, toFollowUsername):
    query = """
    MATCH (c:User{name:$username}), (f:User{name:$toFollowUsername})
    CREATE (c)-[r:FOLLOWS]->(f)
    """

    formatter = {"username": username, "toFollowUsername": toFollowUsername}
    neo.run(query, formatter)

def unfollowUserDAO(username, toUnfollowUsername):
    query = """
    MATCH (c:User{name:$username})-[r:FOLLOWS]->(f:User{name:$toUnfollowUsername})
    DELETE r
    """

    formatter = {"username": username, "toUnfollowUsername": toUnfollowUsername}
    neo.run(query, formatter)