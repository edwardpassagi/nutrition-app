import sys
sys.path.insert(1, './')
import src.beans.NutrientBean as nutrientBean

class NutrientDoseBean(nutrientBean.NutrientBean):
    max_age = 0
    gender = "IDC"
    pregnant = False
    nursing = False
    LB = 0
    IA = 0
    UB = 0

    def __init__(self):
        super().__init__()
        return 

    # The following are setters

    def setNutrientDoseMaxAge(self, newMaxAge):
        self.max_age = newMaxAge

    def setNutrientDoseGender(self, newGender):
        self.gender = newGender

    def setNutrientDoseIsPregnant(self, newIsPregnant):
        self.pregnant = newIsPregnant

    def setNutrientDoseIsNursing(self, newIsNursing):
        self.nursing = newIsNursing

    def setNutrientDoseLB(self, newLB):
        self.LB = newLB

    def setNutrientDoseIA(self, newIA):
        self.IA = newIA
    
    def setNutrientDoseUB(self, newUB):
        self.UB = newUB

    # The following are getters

    def getNutrientDoseMaxAge(self):
        return self.max_age

    def getNutrientDoseGender(self):
        return self.gender

    def getNutrientDoseIsPregnant(self):
        return self.pregnant

    def getNutrientDoseIsNursing(self):
        return self.nursing

    def getNutrientDoseLB(self):
        return self.LB

    def getNutrientDoseIA(self):
        return self.IA
    
    def getNutrientDoseUB(self):
        return self.UB

    