-- TABLE CREATION
CREATE TABLE plan_contains
(
  plan_id INT NOT NULL,
  meal_id INT NOT NULL
);


-- INSERT VALUES
INSERT INTO plan_contains(plan_id, meal_id)
VALUES(1,1);