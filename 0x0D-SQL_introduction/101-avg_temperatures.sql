-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Calculate the average temperature in Fahrenheit by city
USE hbtn_0c_0;
SELECT city, AVG(value) AS average_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
