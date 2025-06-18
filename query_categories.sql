SELECT
    c.name AS category,
    COUNT(fc.film_id) AS number_of_movies
FROM
    category c
LEFT JOIN
    film_category fc ON c.category_id = fc.category_id
GROUP BY
    c.name
ORDER BY
    number_of_movies DESC;
