-- script that displays the max temperature of each state (ordered by State name).
-- Find the max temperature for each state, ordered by state name
SELECT state, MAX(value) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
