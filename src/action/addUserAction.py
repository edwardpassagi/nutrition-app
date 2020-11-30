import sys
from src.beans.UserBean import UserBean
sys.path.insert(1, './')
import src.dao.addUserDAO as addUserDAO
import src.dao.processUserHealthInfoDAO as userHealthInfoDAO
import src.beans.UserBean as userBean

BMR_MEN_INITIAL_VALUE = 66
BMR_MEN_WEIGHT_COEFFECIENT = 6.23
BMR_MEN_HEIGHT_COEFFECIENT = 12.7
BMR_MEN_AGE_COEFFECIENT = 6.8

BMR_WOMEN_INITIAL_VALUE = 655
BMR_WOMEN_WEIGHT_COEFFECIENT = 4.35
BMR_WOMEN_HEIGHT_COEFFECIENT = 4.7
BMR_WOMEN_AGE_COEFFECIENT = 4.7

BMI_WEIGHT_COEFFECIENT = 703

def addNewUser(user: UserBean):    
    user_id = addUserDAO.addUser()
    user.setUserID(user_id)
    user.setBMI(calculateBMI(user.getHeight(), user.getWeight()))
    user.setBMR(calculateBMR(user.getGender(), (2020 - user.getBirthYear()), user.getHeight(), user.getWeight()))
    addUserDAO.editUserInfo(user)
    
    return 

def calculateBMI(height, weight):
    bmiValue = (BMI_WEIGHT_COEFFECIENT * weight)/(height * height)
    return bmiValue

def calculateBMR(gender, age, height, weight):
    bmrValue = 0.0
    if gender == "M" or gender == "IDC":
        bmrValue = BMR_MEN_INITIAL_VALUE + (BMR_MEN_WEIGHT_COEFFECIENT * weight) + (BMR_MEN_HEIGHT_COEFFECIENT * height) - (BMR_MEN_AGE_COEFFECIENT * age)
    elif gender == "F":
        bmrValue = BMR_WOMEN_INITIAL_VALUE + (BMR_WOMEN_WEIGHT_COEFFECIENT * weight) + (BMR_WOMEN_HEIGHT_COEFFECIENT * height) - (BMR_WOMEN_AGE_COEFFECIENT * age)
    return bmrValue 