-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL serve
-- Create the database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table cities if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
