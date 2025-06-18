SELECT
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS employee_name,
    s.store_id,
    YEAR(r.rental_date) AS rental_year,
    COUNT(r.rental_id) AS movies_rented
FROM
    staff s
LEFT JOIN
    rental r ON s.staff_id = r.staff_id
GROUP BY
    s.staff_id, rental_year, s.store_id, employee_name
ORDER BY
    s.staff_id, rental_year;
