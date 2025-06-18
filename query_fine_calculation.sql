SELECT 
    p.rental_id,
    p.customer_id,
    r.rental_date,
    r.return_date,
    ROUND(p.amount * 0.01 * (DATEDIFF(r.return_date, r.rental_date) - 14), 2) AS fine
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id
WHERE r.return_date IS NOT NULL
  AND DATEDIFF(r.return_date, r.rental_date) > 14;
-- doesn't display anything if the fine is 0