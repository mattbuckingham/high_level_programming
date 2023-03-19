-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS `genre`, COUNT(genre_id) AS `number_of_shows`
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
