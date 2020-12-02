from typing import List
from src.beans.NutrientBean import NutrientBean
import sys
sys.path.insert(1, './')
from src.enum.NutrientsEnum import NutrientNameEnum

class FoodBean():
    # fdc_id = 0
    # description = ""
    # food_category_id = 0
    # brand_owner = ""
    # ingredients = ""
    # serving_size = ""
    # serving_size_unit = ""
    # household_serving_fulltext = ""
    # branded_food_category = ""
    # total_protein_amount = ""
    # total_carbohydrates_amount = ""
    # total_fat_amount = ""
    # total_energy_amount = ""
    # nutrients_amounts = [] # list of NutrientBean class
    
    def __init__(self):
        self.fdc_id = 0
        self.description = ""
        self.food_category_id = 0
        self.brand_owner = ""
        self.ingredients = ""
        self.serving_size = ""
        self.serving_size_unit = ""
        self.household_serving_fulltext = ""
        self.branded_food_category = ""
        self.total_protein_amount = ""
        self.total_carbohydrates_amount = ""
        self.total_fat_amount = ""
        self.total_energy_amount = ""
        self.nutrients_amounts = [] # list of NutrientBean class 

    # the following are setters

    def setBrandedFoodFdcID(self, newFDC):
        self.fdc_id = newFDC

    def setBrandedFoodDescription(self, newDescription):
        self.description = newDescription

    def setBrandedFoodCategoryID(self, newCategroyID):
        self.food_category_id = newCategroyID

    def setBrandedFoodBrandOwner(self, newBrandOwner):
        self.brand_owner = newBrandOwner

    def setBrandedFoodIngredients(self, newIngredients):
        self.ingredients = newIngredients
    
    def setBrandedFoodServingSize(self, newServingSize):
        self.serving_size = newServingSize

    def setBrandedFoodServingSizeUnit(self, newServingSizeUnit):
        self.serving_size_unit = newServingSizeUnit

    def setBrandedFoodHouseholdServingFulltext(self, newServingFulltext):
        self.household_serving_fulltext = newServingFulltext

    def setBrandedFoodCategoryDesc(self, newCategroyDesc):
        self.branded_food_category = newCategroyDesc

    def setBrandedFoodProteinAmount(self, newProteinAmount):
        self.total_protein_amount = newProteinAmount

    def setBrandedFoodCarbohydratesAmount(self, newCarbohydratesAmounts):
        self.total_carbohydrates_amount = newCarbohydratesAmounts

    def setBrandedFoodFatAmount(self, newFatAmount):
        self.fdc_id = newFatAmount

    def setBrandedFoodEnergyAmount(self, newEnergyAmount):
        self.total_energy_amount = newEnergyAmount

    def setBrandedFoodNutrientsAmounts(self, newNutrientsAmounts):
        self.nutrients_amounts = newNutrientsAmounts

    def setBrandedFoodNutrientCalories(self, amount):
        return self.setBrandedFoodNutrientAmountByID(1008, amount)

    def setBrandedFoodNutrientAmountByID(self, id: int, newNutrientAmount):
        for element in self.nutrients_amounts:
            if element.getNutrientID() == id:
                element.setNutrientAmount(newNutrientAmount)
            

    # the following are getters

    def getBrandedFoodFdcID(self):
        return self.fdc_id

    def getBrandedFoodDescription(self):
        return self.description

    def getBrandedFoodCategoryID(self):
        return self.food_category_id

    def getBrandedFoodBrandOwner(self):
        return self.brand_owner

    def getBrandedFoodIngredients(self):
        return self.ingredients
    
    def getBrandedFoodServingSize(self):
        return self.serving_size

    def getBrandedFoodServingSizeUnit(self):
        return self.serving_size_unit

    def getBrandedFoodHouseholdServingFulltext(self):
        return self.household_serving_fulltext

    def getBrandedFoodCategoryDesc(self):
        return self.branded_food_category

    def getBrandedFoodProteinAmount(self):
        return self.total_protein_amount

    def getBrandedFoodCarbohydratesAmount(self):
        return self.total_carbohydrates_amount

    def getBrandedFoodFatAmount(self):
        return self.fdc_id

    def getBrandedFoodEnergyAmount(self):
        return self.total_energy_amount

    def getBrandedFoodNutrientsAmounts(self):
        return self.nutrients_amounts

    def getBrandedFoodNutrientAmountByID(self, id: int):
        for element in self.nutrients_amounts:
            if element.getNutrientID() == id:
                return element.getNutrientAmount()

    def getBrandedFoodNutrientCalories(self):
        return self.getBrandedFoodNutrientAmountByID(1008)