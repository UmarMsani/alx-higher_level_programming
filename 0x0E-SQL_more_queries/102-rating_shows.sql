-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
     ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv.title
ORDER BY rating DESC
