-- TABLE CREATION
CREATE TABLE plan
(
  plan_id     INT NOT NULL AUTO_INCREMENT,
  plan_name   VARCHAR(255) NOT NULL, 
  plan_calories INT,
  PRIMARY KEY (plan_id)
);

-- DATA VALUES
INSERT INTO plan (plan_name, plan_calories)
VALUES ("Workout", 2500);