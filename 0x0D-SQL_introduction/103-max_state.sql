-- script that displays the max temperature of each state (ordered by State name).
-- Find the max temperature for each state, ordered by state name
SELECT state, MAX(temperature) AS max_temperature
FROM temperature
GROUP BY state
ORDER BY state;
