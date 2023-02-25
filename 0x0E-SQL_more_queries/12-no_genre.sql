-- Genre ID by show
-- Query that list all shows contained in hbtn_0d_tvshows.
SELECT tv.title, t.genre_id
FROM tv_shows tv
LEFT JOIN tv_show_genres t
ON tv.id = t.show_id
WHERE t.genre_id IS NULL
ORDER BY 1, 2;
