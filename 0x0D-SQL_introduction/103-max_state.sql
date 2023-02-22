-- Max temperature
-- Query that list states and their max temp.
SELECT state, MAX(value)
FROM temperature
GROUP BY 1
ORDER BY 1;
