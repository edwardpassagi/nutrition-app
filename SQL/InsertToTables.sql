-- INSERT VALUES INTO THE TABLE

-- TODO: IMPORTANT: FOOD TABLE CAN BE IMPORTED BY RUNNING
-- localhost:5000/food/secret_load_food
INSERT INTO food (food_name ,food_image ,food_calories )
VALUES ("Salad", "salad.com", 123);
INSERT INTO food (food_name ,food_image ,food_calories )
VALUES ("Milk", "milk.com", 123);
INSERT INTO food (food_name ,food_image ,food_calories )
VALUES ("Banana", "banana.com", 123);

INSERT INTO meal (meal_name, meal_calories)
VALUES ("Breakfast", 450);
INSERT INTO meal (meal_name, meal_calories)
VALUES ("Lunch", 1200);
INSERT INTO meal (meal_name, meal_calories)
VALUES ("Dinner", 700);

INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,1);
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,2);
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,3);

INSERT INTO plan (plan_name, plan_calories)
VALUES ("Workout", 2500);

INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,1);
INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,2);
INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,3);


