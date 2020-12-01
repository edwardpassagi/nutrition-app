from src.enum.NutrientsEnum import NutrientNameEnum
import sys
sys.path.insert(1, './')
import src.dao.generateAIDAO as g_ai_dao

import src.action.processMealAction as processMealAction
import src.action.processFoodAction as processFoodAction
import src.action.processPlanAction as processPlanAction

mealNameBase = ["Breakfast","Lunch","Dinner","Snack"]

def generatePlanAI(planName: str, numMeal:int, pid:int = -1):
    """Generate `numMeal` amount of meals, that is based on the planName

    Args:
        planName (str): The name of the plan (i.e. Workout, Diet)
        numMeal (int): The number of meals that will be generated by our ai

    Returns:
        (void)
    """
    # FIXME: hardcode nummeal if its not between 0-3
    if numMeal > 4 or numMeal <= 0: numMeal = 3

    # FIXME: Plan calories is still hardcoded to 5000
    planCalories = 0

    # TODO: Generate a plan if pid = -1
    if pid == -1:
        planID = g_ai_dao.createNewPlanSQL(planName, planCalories)
    else:
        planID = pid
        planName = processPlanAction.getPlanById(pid)[0]['plan_name']


    # TODO: Link plan with all of the meals
    for eachMeal in range(numMeal):
        mealID = generateMeal(planName, eachMeal)

        # get meal_id and add calories to planID's planCalories
        meal = processMealAction.getMealByMealId(mealID)
        mealCalories = meal[0]['meal_calories']
        print("MEAL CALORIES: {}".format(mealCalories))
        updateVal = "+" + str(mealCalories)

        processPlanAction.updatePlanCaloriesByPlanId(planID, updateVal)

        g_ai_dao.linkMealIDtoPlanID(planID, mealID)

    return

def generateMeal(planName: str, mealNum: int):
    """Generate Meal based on the name of the plan

    Args:
        planName (str): The name of the plan
        mealName (str): Current meal number

    Returns:
        mealID (list): returns the newly created mealID after its linked to the foods len(mealID) is either 3 / 4 (randomized)
    """
    numFoods = 3
    foodIDs = []
    mealName = planName + " " + mealNameBase[mealNum]
    print("mealname: {}".format(mealName))

    # FIXME: calorieTotal should sum all calories from food
    calorieTotal = 0

    # TODO: make new meal that consists of all the foodIDs, catch error
    mealID = processMealAction.createNewMeal(mealName, calorieTotal)

    # TODO: link mealID with all of the foodID
    for eachFood in range(numFoods):
        # TODO: REMOVE HARDCODED VALUES
        # foodID = generateFood(planName)
        foodID = eachFood + 1

        # get food_id and add calories to mealID's mealCalories
        food = processFoodAction.getFoodById(foodID)
        foodCalories = food[0]['food_calories']
        updateVal = "+" + str(foodCalories)

        processMealAction.updateMealCaloriesById(mealID, updateVal)
        g_ai_dao.linkFoodIdToMealId(mealID,foodID)
    return mealID


def generateFood(planName: str):
    """ Find a singular foodID that matches the theme of the planName

    Args:
        planName (str): The name of the plan
    
    Returns:
        foodID (int): The ID of the food that corresponds to the theme of the planName.
    """

    "STEAK ABALLONE"

    # TODO: IMPLEMENT AI ALGORITHM HERE
    # .....

    
    return 1