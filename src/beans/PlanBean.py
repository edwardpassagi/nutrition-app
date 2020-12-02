from src.beans.FoodBean import FoodBean
from src.enum.NutrientsEnum import NutrientNameEnum
import sys
from typing import List
sys.path.insert(1, './')


class PlanBean():
    plan_id = 0
    name = ""
    totalCalories = 0
    mScore = 0
    foodList = []
    nutrientsAmounts = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0.0, 
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

    nutrientsDenied = {NutrientNameEnum.CALCIUM_CONSTANT.value[1]: 0, 
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
    
    def __init__(self):
        return

    def setNutrientAmountByID(self, id, amount):
        self.nutrientsAmounts[id] = amount

    def addNutrientAmountByID(self, id, amount):
        self.nutrientsAmounts[id] += amount

    def subtractNutrientAmountByID(self, id, amount):
        self.nutrientsAmounts[id] -= amount

    def clearAllNutrientAmounts(self):
        for nutrient in self.nutrientsAmounts:
            self.nutrientsAmounts[nutrient] = 0.0

    def clearAllNutrientAmounts(self):
        for nutrient in self.nutrientsDenied:
            self.nutrientsDenied[nutrient] = 0.0

    def incraseNumberOfNutrientDeniesByID(self, id):
        self.nutrientsDenied[id] += 1


    # the following are getters

    def getPlanID(self):
        return self.plan_id

    def getPlaneName(self):
        return self.name

    def getTotalCalories(self):
        return self.totalCalories

    def getNutrientsAmounts(self):
        return self.nutrientsAmounts

    def getNutrientAmountByID(self, id):
        return self.nutrientsAmounts[id]

    def getNutrientsDenied(self):
        return self.nutrientsDenied

    def getNumberofDeniesForNutrientByID(self, id):
        return self.nutrientsDenied[id]