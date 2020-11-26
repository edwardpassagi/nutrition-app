import sys
sys.path.insert(1, './')
import pymysql
import json
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect

import api_handler

from src.action.ProcessDataAction import processDataIntoDatabase

import src.ai.generateAI as gai
import src.action.processPlanAction as processPlanAction
import src.action.processMealAction as processMealAction
import src.action.processFoodAction as processFoodAction
import src.action.processMealContainsAction as processMealContainsAction
import src.action.processPlanContainsAction as processPlanContainsAction

########## VIEW ##########
@app.route('/')
def show_plans():
    plans = processPlanAction.getAllPlans()
    return render_template('home.html', plans=plans)

@app.route('/details/planid:<int:id>')
def show_meals(id):
    plans = processPlanAction.getAllPlans()
    meals = processMealAction.getMealsByPlanID(id)
    return render_template('home.html', plans=plans, planID=id, meals = meals)
    
@app.route('/details/planid:<int:pid>/mealid:<int:mid>')
def show_food_in_meal(pid,mid):
    plans = processPlanAction.getAllPlans()
    meals = processMealAction.getMealsByPlanID(pid)
    foods = processFoodAction.getFoodsByMealID(mid)
    return render_template('home.html', plans=plans, planID=pid, meals = meals, mealID = mid, foods = foods)

    
########## PLAN ##########
# Generate Plan
@app.route('/plan/generate', methods=['POST'])
def generate_plan():
    plan_name = request.form['planName']
    plan_num_meals = request.form['planNumMeals']
    gai.generatePlanAI(plan_name, int(plan_num_meals))
    return redirect('/')

# Delete Plan
@app.route('/plan/delete/<int:id>')
def delete_plan_by_id(id):
    processPlanAction.deletePlanById(id)
    return redirect('/')

# TODO: Create Empty Plan
@app.route('/plan/create', methods=['POST'])
def create_plan():
    plan_name = request.form['planName']
    processPlanAction.createNewPlan(plan_name)
    return redirect('/')



########## MEAL ##########
@app.route('/remove/planid:<int:pid>/mealid:<int:mid>')
def remove_meal(pid,mid):
    processMealAction.removeMealByID(pid, mid)
    return redirect('/details/planid:{}'.format(pid))


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


# TODO: Create food to a meal
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


if __name__ == "__main__":
    # processDataIntoDatabase()
    app.run()