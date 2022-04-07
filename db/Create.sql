CREATE TABLE IF NOT EXISTS foods (
    id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(50) NOT NULL,
    prep_time VARCHAR(50) NOT NULL,
    food_name VARCHAR(500) NOT NULL,
    date_generated DATE NOT NULL
);