-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Select records with names and order by score
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
