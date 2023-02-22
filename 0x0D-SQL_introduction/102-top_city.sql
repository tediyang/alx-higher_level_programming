-- Top 3 cities
-- Query that display cities with high temp during july and aug
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month BETWEEN 6 AND 9
GROUP BY 1,
ORDER BY 2 DESC
LIMIT 3;
