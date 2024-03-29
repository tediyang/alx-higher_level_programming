-- Script that lists shows by their rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY 1
ORDER BY 2 DESC;
