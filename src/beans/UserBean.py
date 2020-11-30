import sys
sys.path.insert(1, './')

class UserBean():
    user_id = 0
    userName = ""
    first_name = ""
    last_name = ""
    password = ""
    email = ""
    gender = "IDC"
    birthYear = 0
    user_decision = "MAINTAIN"
    weight = 0.0
    target_weight = 0.0
    target_timeframe = 0
    height = 0
    daily_activity = "LIGHT"
    is_pregnant = False
    is_nursing = False
    BMI = 0.0
    BMR = 0.0
    daily_maintain_calories = 0.0
    daily_adjusted_calories = 0.0

    def __init__(self):
        return 
    
    # The Following are setters

    def setUserID(self, newID):
        self.user_id = newID

    def setUsername(self, newUsername):
        self.userName = newUsername
    
    def setFirstName(self, newFirstName):
        self.first_name = newFirstName
    
    def setLastName(self, newLastName):
        self.last_name = newLastName

    def setPassword(self, newPassword):
        self.password = newPassword

    def setEmail(self, newEmail):
        self.email = newEmail

    def setGender(self, newGender):
        self.gender = newGender

    def setBirthYear(self, newBirthYear):
        self.birthYear = newBirthYear

    def setUserDecision(self, newUserDecision):
        self.user_decision = newUserDecision
    
    def setWeight(self, newWeight):
        self.weight = newWeight

    def setTargetWeight(self, newTargetWeight):
        self.tarset_weight = newTargetWeight

    def setTargetTimeFrame(self, newTargetTimeFrame):
        self.tarset_timeframe = newTargetTimeFrame

    def setHeight(self, newHeight):
        self.height = newHeight

    def setDailyActivity(self, newDailyActivity):
        self.daily_activity = newDailyActivity

    def setIsPregnant(self, newIsPregnant):
        self.is_pregnant = newIsPregnant

    def setIsNursing(self, newIsNursing):
        self.is_nursing = newIsNursing

    def setBMI(self, newBMI):
        self.BMI = newBMI

    def setBMR(self, newBMR):
        self.BMR = newBMR

    def setDailyMaintainCalories(self, newDailyMaintainCalories):
        self.daily_maintain_calories = newDailyMaintainCalories

    def setDailyAdjustedCalories(self, newDailyAdjustedCalories):
        self.daily_adjusted_calories = newDailyAdjustedCalories

    # The Following are getters

    def getUserID(self):
        return self.user_id
    
    def getUsername(self):
        return self.userName

    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getGender(self):
        return self.gender

    def getBirthYear(self):
        return self.birthYear

    def getUserDecision(self):
        return self.user_decision
    
    def getWeight(self):
        return self.weight

    def getTargetWeight(self):
        return self.target_weight

    def getTargetTimeFrame(self):
        return self.target_timeframe

    def getHeight(self):
        return self.height

    def getDailyActivity(self):
        return self.daily_activity

    def getIsPregnant(self):
        return self.is_pregnant

    def getIsNursing(self):
        return self.is_nursing

    def getBMI(self):
        return self.BMI

    def getBMR(self):
        return self.BMR

    def getDailyMaintainCalories(self):
        return self.daily_maintain_calories

    def getDailyAdjustedCalories(self):
        return self.daily_adjusted_calories