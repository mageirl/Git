SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    CONCAT(a.address, ', ', a.postal_code, ', ', ci.city, ', ', co.country) AS full_address,
    r.rental_date
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE YEAR(r.rental_date) = (
    SELECT MAX(YEAR(rental_date)) FROM rental
)
ORDER BY r.rental_date DESC;
