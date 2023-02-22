-- Best Score
-- Query used to show best score >= 10.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY 1 DESC;
