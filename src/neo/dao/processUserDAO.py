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
