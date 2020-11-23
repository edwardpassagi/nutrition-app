import pymysql
import json
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect

import api_handler


@app.route('/')
def show_plans():
    """Show initial page while only showing plans (if no other thing is passed)

    Returns:
        plans: an array of plan objects returned by the SQL query from the plan table
    """
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM plan")
        plans = cursor.fetchall()

        return render_template('home.html', plans=plans)
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

@app.route('/showMealForPlan/<int:id>')
def show_meals(id):
    """Show meals that makes the plan (if no other thing is passed)

        Returns:
            plans: an array of meal objects returned by the SQL query from the plan table
        """
    conn = None
    cursor = None

    try:
        # Get plans
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM plan")
        plans = cursor.fetchall()

        get_meal_from_plan_cmd = "SELECT meal_name, meal_calories FROM plan NATURAL JOIN plan_contains pc NATURAL JOIN meal m where plan_id = {};".format(str(id))
        cursor.execute(get_meal_from_plan_cmd)
        meals = cursor.fetchall()

        print(meals)
        
        # if not found

        return render_template('home.html', plans=plans, meals = meals)
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


# @app.route('/foods')
# def show_foods():
#     conn = None
#     cursor = None
    
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT * FROM food")
#         rows = cursor.fetchall()

#         return render_template('home.html', rows=rows)
    
#     except Exception as e:
#         print(e)
    
#     finally:
#         cursor.close()
#         conn.close()



# CREATE
# When a user wants to add a new entry
@app.route('/food/new_food')
def add_food_view():
    return render_template('food/food_add.html')

@app.route('/food/add', methods=['POST'])
def add_food():
    conn = None
    cursor = None

    try:
        food_name = request.form['foodName']
        food_image = request.form['foodImage']
        food_calories = request.form['foodCalories']
        print(food_name, food_image, food_calories)

        # validate received value
        if food_name and food_image and food_calories and request.method == 'POST':
            sql = "INSERT INTO food (food_name,food_image, food_calories) VALUES(%s,%s,%s)"

            data = (food_name, food_image, food_calories,)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash('Succesfully added food')
            return redirect('/foods')
        else:
            return 'Invalid food input'
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()



# READ
@app.route('/foods')
def show_foods():
    conn = None
    cursor = None
    
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM food")
        rows = cursor.fetchall()

        return render_template('home.html', rows=rows)
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# EDIT/UPDATE
@app.route('/food/edit/<int:id>')
def edit_view(id):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM food WHERE food_id=%s", id)
        row = cursor.fetchone()

        if row:
            return render_template('food/food_edit.html', row=row)
        else:
            return 'Error loading id:#{}'.format(id=id)

    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


@app.route('/food/update', methods=['POST'])
def update_food():
    conn = None
    cursor = None

    try:
        _food_name = request.form['foodName']
        _food_image = request.form['foodImage']
        _food_calories = request.form['foodCalories']
        _id = request.form['food_id']

        # validate received value
        if _food_name and _food_image and _food_calories and _id and request.method == 'POST':
            sql = "UPDATE food SET food_name=%s, food_image=%s, food_calories=%s WHERE food_id = %s"

            data = (_food_name, _food_image, _food_calories, _id,)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash('Succesfully updated food')
            return redirect('/foods')
        else:
            return 'Error when updating food'
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# delete method
@app.route('/food/delete/<int:id>')
def delete_food(id):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM food WHERE food_id=%s", (id,))
        conn.commit()
        flash('Succesfully deleted food')
        return redirect('/foods')
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# Search method
@app.route('/food/search', methods=['post'])
def search_food():
    conn = None
    cursor = None   

    try:
        _name_hint = request.form['foodHint']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        print(_name_hint)
        if _name_hint:
            sql = "SELECT * FROM food WHERE food_name LIKE '%{}%'".format(_name_hint)
            cursor.execute(sql)

            rows = cursor.fetchall()
            msg = "Search result for: {}".format(_name_hint)
            return render_template('food/food.html', rows=rows, msg=msg)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# FETCH DATA FROM API AND LOAD TO TABLE
@app.route('/food/secret_load_food')
def load_food():
    try:
        load_data_to_tables()
        return redirect('/foods')
    except Exception as e:
        print(e)


def load_data_to_tables():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        food_array = api_handler()
        for item in food_array:
            name, image, calorie_count = get_item_data(item)
            # validate received value
            if name and image and calorie_count:
                sql = "INSERT INTO food (food_name,food_image, food_calories) VALUES(%s,%s,%s)"
                data = (name, image, calorie_count)
                cursor.execute(sql,data)
                conn.commit()
                flash('Succesfully added food')
            else:
                return 'Invalid food input'
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_item_data(item):
    name = item.get('description')
    image = "/" + name + ".jpg"
    calories = 0.0
    foodNutrients = item.get('foodNutrients')
    for nutrient in foodNutrients:
        calories += nutrient.get('amount')
    return name, image, calories


# FIXME: Meals handler

if __name__ == "__main__":
    app.run()