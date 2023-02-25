-- Only Comedy
-- Query that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv.title
FROM tv_shows tv
JOIN tv_show_genres tsg
ON tv.id = tsg.show_id
JOIN tv_genres tg
ON tg.id = tsg.genre_id
WHERE tg.name = "Comedy"
ORDER BY 1;
