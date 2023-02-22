-- Group scores
-- Query that group scores
SELECT score, COUNT(*) number
FROM second_table
GROUP BY 1
ORDER BY 2 DESC;
