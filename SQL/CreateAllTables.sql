-- CREATE ALL DB TABLES
CREATE TABLE food
(
  food_id     INT NOT NULL AUTO_INCREMENT,
  fdc_id INT default 0,
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
  plan_id     INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  plan_name   VARCHAR(255) NOT NULL, 
  plan_calories INT
);

-- CREATE TABLE fdfood (
--     fdc_id INTEGER PRIMARY KEY,
--     data_type LONGTEXT,
--     description LONGTEXT,
--     food_category_id LONGTEXT,
--     publication_date DATETIME
-- );

-- CREATE TABLE foundation_food (
--     fdc_id INTEGER PRIMARY KEY,
--     NDB_number INTEGER,
--     footnote LONGTEXT
-- );

-- CREATE TABLE input_food (
--     id INTEGER PRIMARY KEY,
--     fdc_id INTEGER,
--     fdc_id_of_input_food INTEGER,
--     seq_num INTEGER,
--     amount DOUBLE,
--     sr_code INTEGER,
--     sr_description LONGTEXT,
--     unit VARCHAR(255),
--     portion_code INTEGER,
--     portion_description VARCHAR(255),
--     gram_weight DOUBLE,
--     retention_code INTEGER,
--     survey_flag VARCHAR(255)
-- );

-- CREATE TABLE measure_unit (
--     id INTEGER PRIMARY KEY,
--     name VARCHAR(255)
-- );

-- CREATE TABLE nutrient (
--     id INTEGER PRIMARY KEY,
--     name VARCHAR(255),
--     unit_name VARCHAR(255),
--     nutrient_nbr INTEGER,
--     nutrient_rank INTEGER
-- );

-- CREATE TABLE branded_food (
--     fdc_id INTEGER PRIMARY KEY,
--     brand_owner VARCHAR(255),
--     gtin_upc VARCHAR(255),
--     ingredients LONGTEXT,
--     serving_size INTEGER,
--     serving_size_unit VARCHAR(255),
--     household_serving_fulltext VARCHAR(255),
--     branded_food_category VARCHAR(255),
--     data_source VARCHAR(255),
--     modified_date DATETIME,
--     available_date DATETIME,
--     market_country VARCHAR(255),
--     discontinued_date VARCHAR(255)
-- );

-- CREATE TABLE fndds_derivation (
--     derivation_code VARCHAR(255) PRIMARY KEY,
--     derivation_description LONGTEXT
-- );

-- CREATE TABLE fndds_ingredient_nutrient_value (
--     ingredient_code INTEGER,
--     Ingredient_description LONGTEXT,
--     Nutrient_code INTEGER,
--     Nutrient_value DOUBLE,
--     Nutrient_value_source LONGTEXT,
--     FDC_ID INTEGER,
--     Derivation_code VARCHAR(255),
--     SR_AddMod_year INTEGER,
--     Foundation_year_acquired INTEGER,
--     Start_date DATETIME,
--     End_date DATETIME
-- );

-- CREATE TABLE food_calorie_conversion_factor (
--     food_nutrient_conversion_factor_id INTEGER PRIMARY KEY,
--     protein_value DOUBLE,
--     fat_value DOUBLE,
--     carbohydrate_value DOUBLE
-- );

-- CREATE TABLE food_category (
--     id INTEGER PRIMARY KEY,
--     code INTEGER,
--     description LONGTEXT
-- );

-- CREATE TABLE food_component (
--     id INTEGER PRIMARY KEY,
--     fdc_id INTEGER,
--     name VARCHAR(255),
--     pct_weight DOUBLE,
--     is_refuse VARCHAR(255),
--     gram_weight DOUBLE,
--     data_points INTEGER,
--     min_year_acquired INTEGER
-- );

-- CREATE TABLE food_nutrient_conversion_factor (
--     id INTEGER PRIMARY KEY,
--     fdc_id INTEGER
-- );

-- CREATE TABLE food_nutrient (
--     id INTEGER PRIMARY KEY,
--     fdc_id INTEGER,
--     nutrient_id INTEGER,
--     amount DOUBLE,
--     data_points INTEGER,
--     derivation_id INTEGER,
--     min DOUBLE,
--     max DOUBLE,
--     median DOUBLE,
--     footnote VARCHAR(255),
--     min_year_acquired INTEGER
-- );

-- CREATE TABLE food_portion (
--     id INTEGER PRIMARY KEY,
--     fdc_id INTEGER,
--     seq_num INTEGER,
--     amount DOUBLE,
--     measure_unit_id INTEGER,
--     portion_description VARCHAR(255),
--     modifier VARCHAR(255),
--     gram_weight DOUBLE,
--     data_points INTEGER,
--     footnote VARCHAR(255),
--     min_year_acquired INTEGER
-- );

-- CREATE TABLE food_protein_conversion_factor (
--     food_nutrient_conversion_factor_id INTEGER PRIMARY KEY,
--     value DOUBLE
-- );

-- confirmed table
CREATE TABLE user_info (
	  user_id INT NOT NULL auto_increment PRIMARY KEY,
    username VARCHAR(255) NOT NULL default '',
    first_name VARCHAR(255) NOT NULL default '',
    last_name VARCHAR(255) NOT NULL default '',
    hashed_password VARCHAR(255) default '',
    salt VARCHAR(255) DEFAULT '',
    email VARCHAR(255) default ''
);

-- confirmed table
CREATE TABLE user_health_info (
	  user_id INT NOT NULL primary key,
	  gender enum('M', 'F', 'IDC') default 'IDC',
	  birthYear INT default 0,
    user_decision enum('MAINTAIN', 'LOSE', 'GAIN') default 'MAINTAIN',
	  weight DOUBLE default 0.0,
    target_weight DOUBLE default 0.0,
    target_timeframe INT default 0, -- number of weeks STRICTLY.
    height_inches INT default 0,
    daily_activity enum('SEDENTARY', 'LIGHT', 'MODERATE', 'HARD', 'EXTREME') default 'LIGHT',
    is_pregnant BOOLEAN default FALSE,
    is_nursing BOOLEAN default FALSE,
    BMI DOUBLE default 0.0,
    BMR DOUBLE default 0.0,
    daily_maintain_calories DOUBLE default 0.0,
    daily_adjusted_calories DOUBLE default 0.0
);

-- confirmed table
CREATE TABLE user_nutrient_doses (
	  user_id INT,
    nutrient_id INT,
    LB INT default 0, 
    IA INT default 2500,
    UB INT default 5000,
    weightLowerLB INT NOT NULL default 1,
    default_scoreLowerLB INT NOT NULL default 1,
    weightBetweenLBandIA INT NOT NULL default 1,
    default_scoreBetweenLBandIA INT NOT NULL default 1,
    weightBetweenIAandUB INT NOT NULL default 1,
    default_scoreBetweenIAandUB INT NOT NULL default 1
);


-- confirmed table
CREATE TABLE nutrient_doses (
	  nutrient_id INT, 
    max_age INT,
    gender ENUM('M', 'F', 'IDC'),
    pregnant boolean default false, 
    nursing boolean default false,
    LB INT,
    IA INT,
    UB INT
);

