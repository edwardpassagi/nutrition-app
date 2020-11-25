import sys
sys.path.insert(1, './')

import src.dao.processFoodDAO as processFoodDAO

def getFoodsByMealID(id):
    foods = processFoodDAO.getFoodsByMealIdDAO(id)
    return foods

def getFoodById(id):
    food = processFoodDAO.getFoodById(id)
    return food