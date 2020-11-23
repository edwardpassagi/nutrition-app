-- TABLE CREATION
CREATE TABLE meal_contains
(
  meal_id INT NOT NULL,
  food_id INT NOT NULL
);


-- INSERT VALUES
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,7);
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,11);
INSERT INTO meal_contains(meal_id, food_id)
VALUES(1,17);