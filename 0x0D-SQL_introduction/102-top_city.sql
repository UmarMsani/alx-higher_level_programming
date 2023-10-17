-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Select the top 3 cities with highest temperature in July and August
SELECT city, temperature
FROM your_table_name
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
