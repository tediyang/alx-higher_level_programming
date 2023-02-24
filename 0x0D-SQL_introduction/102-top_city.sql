-- Top 3 cities
-- Query that display cities with high temp during july and aug
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY 1
ORDER BY 2 DESC
LIMIT 3;
