import sys
sys.path.insert(1, './')
from src.beans.UserBean import UserBean
import src.dao.addUserDAO as addUserDAO
import src.dao.processUserHealthInfoDAO as userHealthInfoDAO
import src.dao.processUserNutrientDosesDAO as userNutrientDosesDAO
from src.enum.addUserEnum import BMIvaluesEnum, DailyActivityEnum, DailyAdjustedEnum, GenderEnum, BMRvaluesEnum, UserDecisionEnum
from datetime import date

def addNewUser(user: UserBean):    
    user_id = addUserDAO.addUser()
    user.setUserID(user_id)
    user.setBMI(calculateBMI(user.getHeight(), user.getWeight()))
    user.setBMR(calculateBMR(user.getGender(), (date.today().year - user.getBirthYear()), user.getHeight(), user.getWeight()))
    user.setDailyMaintainCalories(calculateDailyMaintainCalories(user.getDailyActivity(), user.getBMR()))
    user.setDailyAdjustedCalories(calculateDailyAdjustedCalories(user.getUserDecision(), user.getDailyMaintainCalories(), user.getTargetTimeFrame(), abs(user.getTargetWeight() - user.getWeight())))
    addUserDAO.editUserInfo(user)
    userHealthInfoDAO.editUserHealthInfo(user)
    userNutrientDosesDAO.editUserNutrientDoses(user)
    return 

def calculateBMI(height, weight):
    bmiValue = (BMIvaluesEnum.BMI_WEIGHT_COEFFECIENT.value * weight)/(height * height)
    return round(bmiValue, 2)

def calculateBMR(gender, age, height, weight):
    bmrValue = 0.0
    if gender == GenderEnum.MALE.value or gender == GenderEnum.IDC.value:
        bmrValue = BMRvaluesEnum.BMR_MEN_INITIAL_VALUE.value + (BMRvaluesEnum.BMR_MEN_WEIGHT_COEFFECIENT.value * weight) + (BMRvaluesEnum.BMR_MEN_HEIGHT_COEFFECIENT.value * height) - (BMRvaluesEnum.BMR_MEN_AGE_COEFFECIENT.value * age)
    elif gender == GenderEnum.FEMALE.value:
        bmrValue = BMRvaluesEnum.BMR_WOMEN_INITIAL_VALUE.value + (BMRvaluesEnum.BMR_WOMEN_WEIGHT_COEFFECIENT.value * weight) + (BMRvaluesEnum.BMR_WOMEN_HEIGHT_COEFFECIENT.value * height) - (BMRvaluesEnum.BMR_WOMEN_AGE_COEFFECIENT.value * age)
    return round(bmrValue, 2)

def calculateDailyMaintainCalories(activityLevel, bmr):
    daily_maintain_calorie = 0.0
    if activityLevel == DailyActivityEnum.DAILY_ACTIVITY_SEDENTARY_CONSTANT.value:
        daily_maintain_calorie = bmr * DailyActivityEnum.DAILY_ACTIVITY_SEDENTARY_COEFFECIENT.value
    elif activityLevel == DailyActivityEnum.DAILY_ACTIVITY_LIGHT_CONSTANT.value:
        daily_maintain_calorie = bmr * DailyActivityEnum.DAILY_ACTIVITY_LIGHT_COEFFECIENT.value
    elif activityLevel == DailyActivityEnum.DAILY_ACTIVITY_MEDIUM_CONSTANT.value:
        daily_maintain_calorie = bmr * DailyActivityEnum.DAILY_ACTIVITY_MEDIUM_COEFFECIENT.value
    elif activityLevel == DailyActivityEnum.DAILY_ACTIVITY_HARD_CONSTANT.value:
        daily_maintain_calorie = bmr * DailyActivityEnum.DAILY_ACTIVITY_HARD_COEFFECIENT.value
    elif activityLevel == DailyActivityEnum.DAILY_ACTIVITY_EXTREME_CONSTANT.value:
        daily_maintain_calorie = bmr * DailyActivityEnum.DAILY_ACTIVITY_EXTREME_COEFFECIENT.value
    return round(daily_maintain_calorie, 2)

def calculateDailyAdjustedCalories(userDecision, maintain_calories, num_weeks, num_pounds):
    total_adjusted_daily_calories = maintain_calories
    if userDecision == UserDecisionEnum.MAINTAIN.value:
        return maintain_calories
    elif userDecision == UserDecisionEnum.LOSE.value or userDecision == UserDecisionEnum.GAIN.value:
        total_amount_calories = DailyAdjustedEnum.CALORIES_PER_ONE_FAT_POUND.value * num_pounds
        total_amount_calories_per_day = total_amount_calories / (num_weeks * DailyAdjustedEnum.NUM_DAYS_PER_WEEK.value)
        total_adjusted_daily_calories -= total_amount_calories_per_day
        if userDecision == UserDecisionEnum.GAIN.value:
            total_adjusted_daily_calories += total_amount_calories_per_day
    return round(total_adjusted_daily_calories, 2)
    