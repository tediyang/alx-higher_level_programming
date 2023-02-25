-- Number of shows by genre
-- Query that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.name genre, COUNT(ts.title) number_of_shows
FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
JOIN tv_shows ts
ON ts.id = tsg.show_id
GROUP BY 1
ORDER BY 2 DESC;
