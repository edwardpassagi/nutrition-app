import pymysql
import json
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect

# CREATE
# When a user wants to add a new entry
@app.route('/new_ingredient')
def add_ingredient_view():
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def add_ingredient():
    conn = None
    cursor = None

    try:
        _ingredient_name = request.form['ingredientName']
        _ingredient_image = request.form['ingredientImage']
        _ingredient_calories = request.form['ingredientCalories']

        # validate received value
        if _ingredient_name and _ingredient_image and _ingredient_calories and request.method == 'POST':
            sql = "INSERT INTO ingredient (ingredient_name,ingredient_image, ingredient_calories) VALUES(%s,%s,%s)"

            data = (_ingredient_name, _ingredient_image, _ingredient_calories)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash('Succesfully added ingredient')
            return redirect('/')
        else:
            return 'Invalid ingredient input'
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# READ
@app.route('/')
def ingredients():
    conn = None
    cursor = None
    
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM ingredient")
        rows = cursor.fetchall()

        return render_template('ingredients.html', rows=rows)
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# UPDATE
@app.route('/edit/<int:id>')
def edit_view(id):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM ingredient WHERE ingredient_id=%s", id)
        row = cursor.fetchone()

        if row:
            return render_template('edit.html', row=row)
        else:
            return 'Error loading id:#{}'.format(id=id)

    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_ingredient():
    conn = None
    cursor = None

    try:
        _ingredient_name = request.form['ingredientName']
        _ingredient_image = request.form['ingredientImage']
        _ingredient_calories = request.form['ingredientCalories']
        _id = request.form['ingredient_id']

        # validate received value
        if _ingredient_name and _ingredient_image and _ingredient_calories and _id and request.method == 'POST':
            sql = "UPDATE ingredient SET ingredient_name=%s, ingredient_image=%s, ingredient_calories=%s WHERE ingredient_id = %s"

            data = (_ingredient_name, _ingredient_image, _ingredient_calories, _id,)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash('Succesfully updated ingredient')
            return redirect('/')
        else:
            return 'Error when updating ingredient'
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# delete method
@app.route('/delete/<int:id>')
def delete_ingredient(id):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ingredient WHERE ingredient_id=%s", (id,))
        conn.commit()
        flash('Succesfully deleted ingredient')
        return redirect('/')
        
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

# Search method
@app.route('/search', methods=['post'])
def search_ingredient():
    print("HELLO::: search called")
    conn = None
    cursor = None   

    try:
        _name_hint = request.form['ingredientHint']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        print(_name_hint)
        if _name_hint:
            sql = "SELECT * FROM ingredient WHERE ingredient_name LIKE '%{}%'".format(_name_hint)
            cursor.execute(sql)

            rows = cursor.fetchall()
            msg = "Search result for: {}".format(_name_hint)
            return render_template('ingredients.html', rows=rows, msg=msg)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run()