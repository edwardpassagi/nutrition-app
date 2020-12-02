import sys
sys.path.insert(1, './')

class UserNutrientDoseBean():
    user_id = 0
    nutrient_id = 0
    LB = 0
    IA = 0
    UB = 0
    weightLowerLB = 0
    defaultScoreLowerLB = 0
    weightBetweenLBandIA = 0
    defaultScoreBetweenLBandIA = 0
    weightBetweenIAandUB = 0
    defaultScoreBetweenIAandUB = 0

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

    def setUserNutreintWeightLowerLB(self, newWeightLowerLB):
        self.weightLowerLB = newWeightLowerLB

    def setUserNutreintWeightBetweenLBandIA(self, newWeightBetweenLBandIA):
        self.weightBetweenLBandIA = newWeightBetweenLBandIA

    def setUserNutreintWeightBetweenIAandUB(self, newWeightBetweenIAandUB):
        self.weightLowerLB = newWeightBetweenIAandUB

    def setUserNutreintDefaultScoreLowerLB(self, newDefaultScoreLowerLB):
        self.defaultScoreLowerLB = newDefaultScoreLowerLB

    def setUserNutreintDefaultScoreBetweenLBandIA(self, newDefaultScoreBetweenLBandIA):
        self.defaultScoreBetweenLBandIA = newDefaultScoreBetweenLBandIA

    def setUserNutreintDefaultScoreBetweenIAandUB(self, newDefaultScoreBetweenIAandUB):
        self.defaultScoreBetweenIAandUB = newDefaultScoreBetweenIAandUB

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

    def getUserNutreintWeightLowerLB(self):
        return self.weightLowerLB

    def getUserNutreintWeightBetweenLBandIA(self):
        return self.weightBetweenLBandIA

    def getUserNutreintWeightBetweenIAandUB(self):
        return self.weightLowerLB

    def getUserNutreintDefaultScoreLowerLB(self):
        return self.defaultScoreLowerLB

    def getUserNutreintDefaultScoreBetweenLBandIA(self):
        return self.defaultScoreBetweenLBandIA

    def getUserNutreintDefaultScoreBetweenIAandUB(self):
        return self.defaultScoreBetweenIAandUB
    