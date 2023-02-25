-- List shows and genres
-- Query that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv.title, tg.name
FROM tv_shows tv
LEFT JOIN tv_show_genres tsg
ON tv.id = tsg.show_id
LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
ORDER BY 1;
