CREATE TABLE ingredient
(
  ingredient_id     INT NOT NULL AUTO_INCREMENT,
  ingredient_name   VARCHAR(255) NOT NULL,       
  ingredient_image  VARCHAR(255),
  ingredient_calories INT,
  PRIMARY KEY     (ingredient_id)
);