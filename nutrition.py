from src.beans.PlanBean import PlanBean
from src.beans.NutrientBean import NutrientBean
from src.beans.UserBean import UserBean
from src.beans.userNutrientDoseBean import UserNutrientDoseBean
import sys
sys.path.insert(1, './')
import pymysql
import json
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect
from src.action.ProcessDataAction import processDataIntoDatabase
import src.ai.generateAI as gai
import src.action.processPlanAction as processPlanAction
import src.action.processMealAction as processMealAction
import src.action.processFoodAction as processFoodAction
import src.action.processMealContainsAction as processMealContainsAction
import src.action.processPlanContainsAction as processPlanContainsAction
import src.action.clearPlanEntriesAction as clearPlanEntriesAction
import src.action.removeMealAction as removeMealAction
import src.beans.UserBean as userBean
import src.action.addUserAction as addUserAction
import src.dao.processUserNutrientDosesDAO as userNutrientDosesDAO
import src.dao.FoodNutrientsDAO as foodNutrientDAO
import time
import src.action.runQueriesAction as QueriesAction


########## VIEW ##########
# Show all plans
@app.route('/')
def show_plans():
    plans = processPlanAction.getAllPlans()
    return render_template('home.html', plans=plans)

# Show all meals in plan
@app.route('/details/planid:<int:id>')
def show_meals(id):
    plans = processPlanAction.getAllPlans()
    meals = processMealAction.getMealsByPlanID(id)
    planName = processPlanAction.getPlanById(id)[0]['plan_name']
    return render_template('home.html', plans=plans, planID=id, planName=planName, meals=meals)

# Show all foods in meal    
@app.route('/details/planid:<int:pid>/mealid:<int:mid>')
def show_food_in_meal(pid,mid):
    plans = processPlanAction.getAllPlans()
    meals = processMealAction.getMealsByPlanID(pid)
    foods = processFoodAction.getFoodsByMealID(mid)
    planName = processPlanAction.getPlanById(pid)[0]['plan_name']
    mealName = processMealAction.getMealByMealId(mid)[0]['meal_name']
    return render_template('home.html', plans=plans, planID=pid, planName=planName, meals=meals, mealID=mid, mealName=mealName, foods=foods)

# Render search result into home.html
@app.route('/search/food', methods=['POST'])
def search_food_keyword():
    pid = int(request.form['planID'])
    mid = int(request.form['mealID'])
    foodKeyword = request.form['foodKeyword']
    plans = processPlanAction.getAllPlans()
    meals = processMealAction.getMealsByPlanID(pid)
    foods = processFoodAction.getFoodsByMealID(mid)
    planName = processPlanAction.getPlanById(pid)[0]['plan_name']
    mealName = processMealAction.getMealByMealId(mid)[0]['meal_name']
    foodResults = processFoodAction.getFoodByKeyword(foodKeyword)
    print(pid,mid)
    
    return render_template('home.html', plans=plans, planID=pid, planName=planName, meals=meals, mealID=mid, mealName=mealName, foods=foods, foodResults = foodResults, foodKeyword = foodKeyword)
    
########## PLAN ##########
# Generate Plan
@app.route('/plan/generate', methods=['POST'])
def generate_plan():
    plan_name = request.form['planName']
    plan_num_meals = request.form['planNumMeals']
    user: UserBean = QueriesAction.createUserTest3()
    gai.generatePlanAI(plan_name, int(plan_num_meals), user)
    return redirect('/')

# Delete Plan
@app.route('/plan/delete/<int:id>')
def delete_plan_by_id(id):
    processPlanAction.deletePlanById(id)
    return redirect('/')

# Create Empty Plan
@app.route('/plan/create', methods=['POST'])
def create_plan():
    plan_name = request.form['planName']
    processPlanAction.createNewPlan(plan_name)
    return redirect('/')

# Update plan name
@app.route('/rename/plan', methods=["POST"])
def rename_plan():
    pid = request.form['planID']
    newPlanName = request.form['planName']
    processPlanAction.renamePlanByPid(pid, newPlanName)
    return redirect('/details/planid:{}'.format(pid))



########## MEAL ##########
# Remove Meal
@app.route('/remove/planid:<int:pid>/mealid:<int:mid>')
def remove_meal(pid,mid):
    removeMealAction.removeMealByID(pid, mid)
    return redirect('/details/planid:{}'.format(pid))

# Regenerate Meal
@app.route('/plan/regenerate', methods=['POST'])
def regenerate_meal():
    plan_num_meals = request.form['planNumMeals']
    pid = request.form['planID']
    # unlink all mid entry from pid
    clearPlanEntriesAction.deletePlanIdEntry(pid)
    # call regenerate AI
    gai.generatePlanAI("", int(plan_num_meals), pid)
    # redirect to plan details
    return redirect('/details/planid:{}'.format(pid))

# Update meal name
@app.route('/rename/meal', methods=["POST"])
def rename_meal():
    pid = request.form['planID']
    mid = request.form['mealID']
    newMealName = request.form['mealName']
    processMealAction.renameMealByMid(mid, newMealName)
    return redirect('/details/planid:{}/mealid:{}'.format(pid,mid))


########## FOOD ##########
# Remove food from meal
@app.route('/food/removeFromMeal/planid:<int:pid>/mealid:<int:mid>/foodid:<int:fid>')
def remove_food_from_meal(pid, mid,fid):
    processMealContainsAction.removeFoodIdFromMealId(mid,fid)
    return redirect('/details/planid:{}/mealid:{}'.format(pid,mid))

# Create blank meal and add to plan
@app.route('/meal/create', methods=['POST'])
def create_empty_meal_to_plan():
    pid = request.form['planID']
    mealName = request.form['mealName']
    mid = processMealAction.createNewMeal(mealName)
    processPlanContainsAction.linkPidToMid(pid,mid)
    return redirect('/details/planid:{}'.format(pid))

# Create New Food Entry
@app.route('/food/create', methods=['POST'])
def create_empty_food_to_meal():
    # Form already validates so that foodName and foodCalories is NOT NULL
    foodName = request.form['foodName']
    foodCalories = request.form['foodCalories']
    pid = request.form['planID']
    mid = request.form['mealID']
    #TODO: Create food instance
    fid = processFoodAction.createNewFood(foodName, foodCalories)
    processMealContainsAction.addFoodIdToMealId(mid,fid)
    return redirect('/details/planid:{}/mealid:{}'.format(pid,mid))

# Link Food to Meal
@app.route('/food/link', methods=['post'])
def link_food_to_meal():
    pid = request.form['planID']
    mid = request.form['mealID']
    fid = request.form['foodID']
    processMealContainsAction.addFoodIdToMealId(mid,fid)  
    return redirect('/details/planid:{}/mealid:{}'.format(pid,mid))

if __name__ == "__main__":
    # do not uncomment the below line unless you are sure of its side effects, 
    # it will clear out all the data.
    # processDataIntoDatabase()
    app.run(host = 'localhost')
