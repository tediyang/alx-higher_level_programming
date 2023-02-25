-- Cities by States
-- Query that list all the cities contained in the database.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON states.id = cities.state_id
ORDER BY 1;
