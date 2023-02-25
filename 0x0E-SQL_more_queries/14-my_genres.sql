-- My genres
-- Query that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tg.name
FROM tv_shows tv
JOIN tv_show_genres tsg
ON tv.id = tsg.show_id
JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tv.title = "Dexter"
ORDER BY 1;
