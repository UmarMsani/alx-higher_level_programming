-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Find the state_id for California
SELECT id FROM states WHERE name = 'California';

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List all cities of California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
