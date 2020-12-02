import sys
sys.path.insert(1, './')

class UserNutrientDoseBean():
    user_id = 0
    nutrient_id = 0
    LB = 0
    IA = 0
    UB = 0
    weight = 0
    default_score = 0

    def __init__(self):
        return 

    # the following are setters

    def setNutrientDoseUserID(self, newUserID):
        self.user_id = newUserID

    def setUserNutrientID(self, newNutrientID):
        self.nutrient_id = newNutrientID

    def setUserNutrientLB(self, newLB):
        self.LB = newLB

    def setUserNutrientIA(self, newIA):
        self.IA = newIA

    def setUserNutrientUB(self, newUB):
        self.UB = newUB

    def setUserNutrientWeight(self, newWeight):
        self.weight = newWeight

    def setUserNutrientDefaultScore(self, newDefaultScore):
        self.default_score = newDefaultScore

    # the following are getters

    def getNutrientDoseUserID(self):
        return self.user_id

    def getUserNutrientID(self):
        return self.nutrient_id

    def getUserNutrientLB(self):
        return self.LB

    def getUserNutrientIA(self):
        return self.IA

    def getUserNutrientUB(self):
        return self.UB

    def getUserNutrientWeight(self):
        return self.weight

    def getUserNutrientDefaultScore(self):
        return self.default_score