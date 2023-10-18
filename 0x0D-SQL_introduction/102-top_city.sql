-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Select the top 3 cities with highest temperature in July and August
SELECT city, AVG(value) AS average_temperature_fahrenheit
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP by city
ORDER BY average_temperature_fahrenheit DESC
LIMIT 3;
