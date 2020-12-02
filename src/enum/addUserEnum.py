from enum import Enum
import sys
sys.path.insert(1, './')

class GenderEnum(Enum):
    MALE = "M"
    FEMALE = "F"
    IDC = "IDC"


class BMRvaluesEnum(Enum):
    BMR_MEN_INITIAL_VALUE = 66
    BMR_MEN_WEIGHT_COEFFECIENT = 6.23
    BMR_MEN_HEIGHT_COEFFECIENT = 12.7
    BMR_MEN_AGE_COEFFECIENT = 6.8

    BMR_WOMEN_INITIAL_VALUE = 655
    BMR_WOMEN_WEIGHT_COEFFECIENT = 4.35
    BMR_WOMEN_HEIGHT_COEFFECIENT = 4.7
    BMR_WOMEN_AGE_COEFFECIENT = 4.7

class BMIvaluesEnum(Enum):
    BMI_WEIGHT_COEFFECIENT = 703

class DailyActivityEnum(Enum):
    DAILY_ACTIVITY_SEDENTARY_COEFFECIENT = 1.2
    DAILY_ACTIVITY_LIGHT_COEFFECIENT = 1.375
    DAILY_ACTIVITY_MEDIUM_COEFFECIENT = 1.55
    DAILY_ACTIVITY_HARD_COEFFECIENT = 1.725
    DAILY_ACTIVITY_EXTREME_COEFFECIENT = 1.9

    DAILY_ACTIVITY_SEDENTARY_CONSTANT = "SEDENTARY"
    DAILY_ACTIVITY_LIGHT_CONSTANT = "LIGHT"
    DAILY_ACTIVITY_MEDIUM_CONSTANT = "MODERATE"
    DAILY_ACTIVITY_HARD_CONSTANT = "HARD"
    DAILY_ACTIVITY_EXTREME_CONSTANT = "EXTREME"

class UserDecisionEnum(Enum):
    MAINTAIN = 'MAINTAIN'
    LOSE = 'LOSE'
    GAIN = 'GAIN'

class DailyAdjustedEnum(Enum):
    CALORIES_PER_ONE_FAT_POUND = 3500
    NUM_DAYS_PER_WEEK = 7