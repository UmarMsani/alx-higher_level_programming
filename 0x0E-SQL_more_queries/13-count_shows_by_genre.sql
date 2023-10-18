-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
    genres.name as genre,
    COUNT(tv_show_genres.show_id) as number_of_shows
FROM
    genres
JOIN
    tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY
    genres.name
HAVING
    number_of_shows > 0
ORDER BY
    number_of_shows DESC;
