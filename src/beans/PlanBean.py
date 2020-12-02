from src.beans.FoodBean import FoodBean
from src.enum.NutrientsEnum import NutrientNameEnum
import sys
from typing import List
sys.path.insert(1, './')


class PlanBean(object):
    # plan_id = 0
    # name = ""
    # totalCalories = 0
    # mScore = 0
    # foodList = []
    # nutrientsAmounts = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0.0, 
    #                         NutrientNameEnum.PHOSPHEROUS_CONSTANT.value[1]: 0.0, 
    #                         NutrientNameEnum.MAGNESIUM_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.POTASSIUM_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.SODIUM_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.IRON_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.MANGANESE_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.COPPER_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.ZINC_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.PANTOTHONIC_ACID_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.NICACIN_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.VITAMIN_A_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.VITAMIN_C_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.VITAMIN_E_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.VITAMIN_K_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.THIAMIN_CONSTANT.value[1]: 0.0,
    #                         NutrientNameEnum.CALORIES_CONSTANT.value[1]: 0.0}

    # nutrientsDenied = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0, 
    #                         NutrientNameEnum.PHOSPHEROUS_CONSTANT.value[1]: 0, 
    #                         NutrientNameEnum.MAGNESIUM_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.POTASSIUM_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.SODIUM_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.IRON_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.MANGANESE_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.COPPER_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.ZINC_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.PANTOTHONIC_ACID_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.NICACIN_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_A_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_C_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_E_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_K_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.THIAMIN_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.CALORIES_CONSTANT.value[1]: 0}
    
    # nutrientsNscore = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0, 
    #                         NutrientNameEnum.PHOSPHEROUS_CONSTANT.value[1]: 0, 
    #                         NutrientNameEnum.MAGNESIUM_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.POTASSIUM_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.SODIUM_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.IRON_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.MANGANESE_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.COPPER_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.ZINC_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.PANTOTHONIC_ACID_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.NICACIN_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_A_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_C_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_E_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.VITAMIN_K_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.THIAMIN_CONSTANT.value[1]: 0,
    #                         NutrientNameEnum.CALORIES_CONSTANT.value[1]: 0}

    def __init__(self):
        self.plan_id = 0
        self.name = ""
        self.totalCalories = 0
        self.mScore = 0
        self.foodList = []
        self.nutrientsAmounts = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0.0, 
                            NutrientNameEnum.PHOSPHEROUS_CONSTANT.value[1]: 0.0, 
                            NutrientNameEnum.MAGNESIUM_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.POTASSIUM_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.SODIUM_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.IRON_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.MANGANESE_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.COPPER_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.ZINC_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.PANTOTHONIC_ACID_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.NICACIN_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.VITAMIN_A_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.VITAMIN_C_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.VITAMIN_E_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.VITAMIN_K_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.THIAMIN_CONSTANT.value[1]: 0.0,
                            NutrientNameEnum.CALORIES_CONSTANT.value[1]: 0.0}

        self.nutrientsDenied = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0, 
                            NutrientNameEnum.PHOSPHEROUS_CONSTANT.value[1]: 0, 
                            NutrientNameEnum.MAGNESIUM_CONSTANT.value[1]: 0,
                            NutrientNameEnum.POTASSIUM_CONSTANT.value[1]: 0,
                            NutrientNameEnum.SODIUM_CONSTANT.value[1]: 0,
                            NutrientNameEnum.IRON_CONSTANT.value[1]: 0,
                            NutrientNameEnum.MANGANESE_CONSTANT.value[1]: 0,
                            NutrientNameEnum.COPPER_CONSTANT.value[1]: 0,
                            NutrientNameEnum.ZINC_CONSTANT.value[1]: 0,
                            NutrientNameEnum.PANTOTHONIC_ACID_CONSTANT.value[1]: 0,
                            NutrientNameEnum.NICACIN_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_A_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_C_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_E_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_K_CONSTANT.value[1]: 0,
                            NutrientNameEnum.THIAMIN_CONSTANT.value[1]: 0,
                            NutrientNameEnum.CALORIES_CONSTANT.value[1]: 0}
    
        self.nutrientsNscore = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0, 
                            NutrientNameEnum.PHOSPHEROUS_CONSTANT.value[1]: 0, 
                            NutrientNameEnum.MAGNESIUM_CONSTANT.value[1]: 0,
                            NutrientNameEnum.POTASSIUM_CONSTANT.value[1]: 0,
                            NutrientNameEnum.SODIUM_CONSTANT.value[1]: 0,
                            NutrientNameEnum.IRON_CONSTANT.value[1]: 0,
                            NutrientNameEnum.MANGANESE_CONSTANT.value[1]: 0,
                            NutrientNameEnum.COPPER_CONSTANT.value[1]: 0,
                            NutrientNameEnum.ZINC_CONSTANT.value[1]: 0,
                            NutrientNameEnum.PANTOTHONIC_ACID_CONSTANT.value[1]: 0,
                            NutrientNameEnum.NICACIN_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_A_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_C_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_E_CONSTANT.value[1]: 0,
                            NutrientNameEnum.VITAMIN_K_CONSTANT.value[1]: 0,
                            NutrientNameEnum.THIAMIN_CONSTANT.value[1]: 0,
                            NutrientNameEnum.CALORIES_CONSTANT.value[1]: 0}

    def setPlanID(self, newPlanID):
        self.plan_id = newPlanID

    def setPlanName(self, newPlanName):
        self.name = newPlanName

    def setFoodList(self, foodList):
        self.foodList = foodList

    def generatePlanTotalCalories(self):
        self.totalCalories = self.getNutrientAmountByID(1008)

    def generatePlanTotalCaloriesBasedOnFood(self):
        for foodItem in self.foodList:
            self.totalCalories += foodItem.getBrandedFoodNutrientCalories()

    def setNutrientAmountByID(self, id, amount):
        self.nutrientsAmounts[id] = amount

    def addNutrientAmountByID(self, id, amount):
        self.nutrientsAmounts[id] += amount

    def subtractNutrientAmountByID(self, id, amount):
        self.nutrientsAmounts[id] -= min(self.nutrientsAmounts[id], amount)

    def clearAllNutrientAmounts(self):
        for nutrient in self.nutrientsAmounts:
            self.nutrientsAmounts[nutrient] = 0.0

    def clearAllNutrientAmounts(self):
        for nutrient in self.nutrientsDenied:
            self.nutrientsDenied[nutrient] = 0.0

    def incraseNumberOfNutrientDeniesByID(self, id):
        self.nutrientsDenied[id] += 1

    def resetNumberOfNutrientDeniesByID(self, id):
        self.nutrientsDenied[id] = 0

    def setNutrientsNScore(self, newNutrientsNScore):
        self.nutrientsNscore = newNutrientsNScore

    def setNutrientNscoreValue(self, nutrient_id, value):
        self.nutrientsNscore[nutrient_id] = value
    
    def setPlanMScore(self, newMscore):
        self.mScore = newMscore

    def increasePlanMScoreBy(self, amount):
        self.mScore += amount

    def setTotalCalories(self, newAmount):
        self.totalCalories = newAmount

    def addFoodItemToList(self, foodItem: FoodBean):
        self.foodList.append(foodItem)

    # the following are getters

    def getPlanID(self):
        return self.plan_id

    def getPlanName(self):
        return self.name

    def getTotalCalories(self):
        # self.totalCalories = self.getNutrientAmountByID(1008)
        return self.totalCalories

    def getPlanFoodList(self):
        return self.foodList

    def getplanFood(self, idx):
        return self.foodList[idx]

    def getNutrientsAmounts(self):
        return self.nutrientsAmounts

    def getNutrientAmountByID(self, id):
        return self.nutrientsAmounts[id]

    def getNutrientsDenied(self):
        return self.nutrientsDenied

    def getNumberofDeniesForNutrientByID(self, id):
        return self.nutrientsDenied[id]

    def getNutrientsNScore(self):
        return self.nutrientsNscore

    def getNutrientNscoreValue(self, nutrient_id):
        return self.nutrientsNscore[nutrient_id]

    def getPlanMScore(self):
        return self.mScore
    