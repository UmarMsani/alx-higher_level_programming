-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Calculate the average temperature in Fahrenheit by city
SELECT city, AVG((temperature * 9/5) + 32) AS average_temperature_fahrenheit
FROM your_table_name
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
