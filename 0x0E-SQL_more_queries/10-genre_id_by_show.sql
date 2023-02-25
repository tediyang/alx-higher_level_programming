-- Genre ID by show
-- Query that list all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv.title, t.genre_id
FROM tv_shows tv
JOIN tv_show_genres t
ON tv.id = t.show_id
ORDER BY 1, 2;
