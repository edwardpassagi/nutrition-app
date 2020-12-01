import sys
sys.path.insert(1, './')

class NutrientBean:
    nutrient_id = 0
    nutrient_name = ""
    nutrient_unit_name = ""
    nutrient_nbr = 0

    def __init__(self):
        return

    def setNutrientID(self, newNutrientID):
        self.nutrient_id = newNutrientID

    def setNutrientName(self, newNutrientName):
        self.nutrient_name = newNutrientName

    def setNutrientUnitName(self, newNutrientUnitName):
        self.nutrient_unit_name = newNutrientUnitName

    def setNutrientNbr(self, newNutrientNbr):
        self.nutrient_nbr = newNutrientNbr

    # The following are getters

    def getNutrientID(self):
        return self.nutrient_id

    def getNutrientName(self):
        return self.nutrient_name;

    def getNutrientUnitName(self):
        return self.nutrient_unit_name

    def getNutrientNbr(self):
        return self.nutrient_nbr

    