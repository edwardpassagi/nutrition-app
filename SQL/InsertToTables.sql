-- INSERT VALUES INTO THE TABLE

-- TODO: IMPORTANT: FOOD TABLE CAN BE IMPORTED BY RUNNING
-- localhost:5000/food/secret_load_food

INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,7);
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,11);
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,17);

INSERT INTO meal (meal_name, meal_calories)
VALUES ("Breakfast", 450);
INSERT INTO meal (meal_name, meal_calories)
VALUES ("Lunch", 1200);
INSERT INTO meal (meal_name, meal_calories)
VALUES ("Dinner", 700);

INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,1);
INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,2);
INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,3);

INSERT INTO plan (plan_name, plan_calories)
VALUES ("Workout", 2500);
