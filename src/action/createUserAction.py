import sys
sys.path.insert(1, './')
import src.dao.createUserDAO as createUserDAO


def createNewUser(userInfo):    
    user_id = createUserDAO.addEmptyUser()
    
    return 