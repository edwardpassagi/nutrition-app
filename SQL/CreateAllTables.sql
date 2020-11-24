-- CREATE ALL DB TABLES
CREATE TABLE food
(
  food_id     INT NOT NULL AUTO_INCREMENT,
  food_name   VARCHAR(255) NOT NULL,       
  food_image  VARCHAR(255),
  food_calories INT,
  PRIMARY KEY     (food_id)
);

CREATE TABLE meal_contains
(
  meal_id INT NOT NULL,
  food_id INT NOT NULL
);

CREATE TABLE meal
(
  meal_id     INT NOT NULL AUTO_INCREMENT,
  meal_name   VARCHAR(255) NOT NULL, 
  meal_calories INT,
  PRIMARY KEY (meal_id)
);

CREATE TABLE plan_contains
(
  plan_id INT NOT NULL,
  meal_id INT NOT NULL
);

CREATE TABLE plan
(
  plan_id     INT NOT NULL AUTO_INCREMENT,
  plan_name   VARCHAR(255) NOT NULL, 
  plan_calories INT,
  PRIMARY KEY (plan_id)
);