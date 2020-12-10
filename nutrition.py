import sys
sys.path.insert(1, './')
from app import app
from flask import render_template, request, redirect

from src.beans.UserBean import UserBean
import src.ai.generateAI as gai
import src.action.ProcessDataAction as ProcessDataAction
import src.action.processPlanAction as processPlanAction
import src.action.processMealAction as processMealAction
import src.action.processFoodAction as processFoodAction
import src.action.processMealContainsAction as processMealContainsAction
import src.action.processPlanContainsAction as processPlanContainsAction
import src.action.clearPlanEntriesAction as clearPlanEntriesAction
import src.action.removeMealAction as removeMealAction
import src.action.runQueriesAction as QueriesAction


import src.neo.action.processUserAction as processUserAction

########## LOGIN LOGIC ##########
# Show login page
@app.route('/')
def show_login():
    return render_template('login.html')

# Login preprocessing
@app.route('/login', methods=["POST"])
def login_processing():
    username = request.form["username"]
    # TODO: check if username doesnt exist, render  login with error message, force user to make a new account
    if processUserAction.isValidUsername(username):
        return redirect("/{}".format(username))
    else:
        return render_template('login.html', error = True)

@app.route('/register', methods=["POST"])
def register_processing():
    username = request.form["username"]
    processUserAction.createNewUserNode(username)
    return redirect("/{}".format(username))

########## VIEW ##########
# Show preferences page for user
@app.route('/<string:username>/preferences')
def show_prefrences(username):
    return render_template("preferences.html", username=username)

# Show all plans
@app.route('/<string:username>')
def show_plans(username):
    if not processUserAction.isValidUsername(username):
        return render_template('login.html', error = True)
    plans = processPlanAction.getAllPlans(username)
    return render_template('home.html', username=username, plans=plans)

# Show all meals in plan
@app.route('/<string:username>/planid:<int:id>')
def show_meals(username, id):
    if not processUserAction.isValidUsername(username):
        return render_template('login.html', error = True)
    plans = processPlanAction.getAllPlans(username)
    meals = processMealAction.getMealsByPlanID(id)
    planName = processPlanAction.getPlanById(id)[0]['plan_name']
    return render_template('home.html', username=username, plans=plans, planID=id, planName=planName, meals=meals)

# Show all foods in meal    
@app.route('/<string:username>/planid:<int:pid>/mealid:<int:mid>')
def show_food_in_meal(username,pid,mid):
    if not processUserAction.isValidUsername(username):
        return render_template('login.html', error = True)
    plans = processPlanAction.getAllPlans(username)
    meals = processMealAction.getMealsByPlanID(pid)
    foods = processFoodAction.getFoodsByMealID(mid)
    planName = processPlanAction.getPlanById(pid)[0]['plan_name']
    mealName = processMealAction.getMealByMealId(mid)[0]['meal_name']
    return render_template('home.html', username=username, plans=plans, planID=pid, planName=planName, meals=meals, mealID=mid, mealName=mealName, foods=foods)

# Render search result into home.html
@app.route('/<string:username>/search/food', methods=['POST'])
def search_food_keyword(username):
    if not processUserAction.isValidUsername(username):
        return render_template('login.html', error = True)
    pid = int(request.form['planID'])
    mid = int(request.form['mealID'])
    foodKeyword = request.form['foodKeyword']
    plans = processPlanAction.getAllPlans(username)
    meals = processMealAction.getMealsByPlanID(pid)
    foods = processFoodAction.getFoodsByMealID(mid)
    planName = processPlanAction.getPlanById(pid)[0]['plan_name']
    mealName = processMealAction.getMealByMealId(mid)[0]['meal_name']
    foodResults = processFoodAction.getFoodByKeyword(foodKeyword, username)
    print(pid,mid)
    
    return render_template('home.html', username=username, plans=plans, planID=pid, planName=planName, meals=meals, mealID=mid, mealName=mealName, foods=foods, foodResults = foodResults, foodKeyword = foodKeyword)
    
########## PLAN ##########
# Generate Plan
@app.route('/<string:username>/plan/generate', methods=['POST'])
def generate_plan(username):
    plan_name = request.form['planName']
    plan_num_meals = request.form['planNumMeals']

    user: UserBean = QueriesAction.createUserTest3()
    pid = gai.generatePlanAI(plan_name, int(plan_num_meals),username, user)
    return redirect('/{}/planid:{}'.format(username, pid))

# Delete Plan
@app.route('/<string:username>/plan/delete/<int:id>')
def delete_plan_by_id(username, id):
    processPlanAction.deletePlanById(id)
    return redirect('/{}'.format(username))

# Create Empty Plan
@app.route('/<string:username>/plan/create', methods=['POST'])
def create_plan(username):
    plan_name = request.form['planName']
    processPlanAction.createNewPlan(plan_name, username)
    return redirect('/{}'.format(username))

# Update plan name
@app.route('/<string:username>/rename/plan', methods=["POST"])
def rename_plan(username):
    pid = request.form['planID']
    newPlanName = request.form['planName']
    processPlanAction.renamePlanByPid(pid, newPlanName)
    return redirect('/{}/planid:{}'.format(username,pid))



########## MEAL ##########
# Remove Meal
@app.route('/<string:username>/remove/planid:<int:pid>/mealid:<int:mid>')
def remove_meal(username, pid,mid):
    removeMealAction.removeMealByID(pid, mid)
    return redirect('/{}/planid:{}'.format(username,pid))

# Regenerate Meal
@app.route('/<string:username>/plan/regenerate', methods=['POST'])
def regenerate_meal(username):
    plan_num_meals = request.form['planNumMeals'] 
    pid = request.form['planID']
    # TODO: dont hardcode user object
    user: UserBean = QueriesAction.createUserTest3()
    # unlink all mid entry from pid
    clearPlanEntriesAction.deletePlanIdEntry(pid)

    # call regenerate AI
    gai.generatePlanAI("", int(plan_num_meals), username, user, pid)
    # redirect to plan details
    return redirect('/{}/planid:{}'.format(username,pid))

# Update meal name
@app.route('/<string:username>/rename/meal', methods=["POST"])
def rename_meal(username):
    pid = request.form['planID']
    mid = request.form['mealID']
    newMealName = request.form['mealName']
    processMealAction.renameMealByMid(mid, newMealName)
    return redirect('/{}/planid:{}/mealid:{}'.format(username,pid,mid))


########## FOOD ##########
# Remove food from meal
@app.route('/<string:username>/food/removeFromMeal/planid:<int:pid>/mealid:<int:mid>/foodid:<int:fid>')
def remove_food_from_meal(username,pid,mid,fid):
    processMealContainsAction.removeFoodIdFromMealId(mid,fid)
    return redirect('/{}/planid:{}/mealid:{}'.format(username,pid,mid))

# Create blank meal and add to plan
@app.route('/<string:username>/meal/create', methods=['POST'])
def create_empty_meal_to_plan(username):
    pid = request.form['planID']
    mealName = request.form['mealName']
    mid = processMealAction.createNewMeal(mealName)
    processPlanContainsAction.linkPidToMid(pid,mid)
    return redirect('/{}/planid:{}'.format(username,pid))

# Create New Food Entry
@app.route('/<string:username>/food/create', methods=['POST'])
def create_empty_food_to_meal(username):
    # Form already validates so that foodName and foodCalories is NOT NULL
    foodName = request.form['foodName']
    foodCalories = request.form['foodCalories']
    pid = request.form['planID']
    mid = request.form['mealID']
    #TODO: Create food instance
    fid = processFoodAction.createNewFood(foodName, foodCalories, username)
    processMealContainsAction.addFoodIdToMealId(mid,fid)
    return redirect('/{}/planid:{}/mealid:{}'.format(username,pid,mid))

# Link Food to Meal
@app.route('/<string:username>/food/link', methods=['post'])
def link_food_to_meal(username):
    pid = request.form['planID']
    mid = request.form['mealID']
    fid = request.form['foodID']
    processMealContainsAction.addFoodIdToMealId(mid,fid)  
    return redirect('/{}/planid:{}/mealid:{}'.format(username,pid,mid))


########## SOCIAL ##########
# Show social feed
@app.route('/<string:username>/social')
def show_social(username):
    followings = processUserAction.getUserFollowings(username)
    followers = processUserAction.getUserFollowers(username)
    nonFolloweds = processUserAction.getNonFollowedUsers(username)
    return render_template('social.html', username=username, followings=followings, followers=followers, nonFolloweds=nonFolloweds)

# Following endpoint
@app.route('/<string:username>/follow/<string:toFollowUsername>')
def follow_user(username, toFollowUsername):
    processUserAction.followUser(username, toFollowUsername)
    return redirect('/{}/social'.format(username))

# Unfollow endpoint
@app.route('/<string:username>/unfollow/<string:toUnfollowUsername>')
def unfollow_user(username, toUnfollowUsername):
    processUserAction.unfollowUser(username, toUnfollowUsername)
    return redirect('/{}/social'.format(username))

########## VIEW ##########
# Show all plans
@app.route('/<string:username>/view/<string:followingUsername>')
def show_friend_plans(username, followingUsername):
    plans = processPlanAction.getAllPlans(followingUsername)
    return render_template('friends_plan.html', username=username, followingUsername=followingUsername, plans=plans)

# Show all meals in plan
@app.route('/<string:username>/view/<string:followingUsername>/planid:<int:id>')
def show_friend_meals(username, followingUsername, id):
    plans = processPlanAction.getAllPlans(followingUsername)
    meals = processMealAction.getMealsByPlanID(id)
    planName = processPlanAction.getPlanById(id)[0]['plan_name']
    return render_template('friends_plan.html', username=username, followingUsername=followingUsername,  plans=plans, planID=id, planName=planName, meals=meals)

# Display 
# Show all foods in meal    
@app.route('/<string:username>/view/<string:followingUsername>/planid:<int:pid>/mealid:<int:mid>')
def show_friend_food_in_meal(username,followingUsername,pid,mid):
    if not processUserAction.isValidUsername(username):
        return render_template('login.html', error = True)
    plans = processPlanAction.getAllPlans(followingUsername)
    meals = processMealAction.getMealsByPlanID(pid)
    foods = processFoodAction.getFoodsByMealID(mid)
    planName = processPlanAction.getPlanById(pid)[0]['plan_name']
    mealName = processMealAction.getMealByMealId(mid)[0]['meal_name']
    return render_template('friends_plan.html', username=username, followingUsername=followingUsername, plans=plans, planID=pid, planName=planName, meals=meals, mealID=mid, mealName=mealName, foods=foods)

if __name__ == "__main__":
    # do not uncomment the below line unless you are sure of its side effects, 
    # it will clear out all the data.
    # ProcessDataAction.processDataIntoDatabase()
    app.run(host = 'localhost')
