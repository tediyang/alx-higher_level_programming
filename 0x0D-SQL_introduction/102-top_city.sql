-- Top 3 cities
-- Query that display cities with high temp during july and aug
SELECT city, AVG(value) avg_temp
FROM temperatures
GROUP BY 1,
HAVING month BETWEEN 7 AND 8
ORDER BY 2 DESC
LIMIT 3;
