-- Cities by States
-- Query that list all the cities contained in the database.
SELECT c.id, c.name cities, s.name states
FROM cities c
JOIN states s
ON s.id = c.state_id
ORDER BY 1;
