-- TABLE CREATION
CREATE TABLE meal
(
  meal_id     INT NOT NULL AUTO_INCREMENT,
  meal_name   VARCHAR(255) NOT NULL, 
  meal_calories INT,
  PRIMARY KEY (meal_id)
);

-- DATA VALUES
INSERT INTO meal (meal_name, meal_calories)
VALUES ("Breakfast", 450)