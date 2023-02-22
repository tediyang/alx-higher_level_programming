-- No link
-- Query that list records with no null value for name column
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
