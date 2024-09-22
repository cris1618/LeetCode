# Write your MySQL query statement below
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM sales AS s
JOIN product AS p ON s.product_id = p.product_id
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM sales
    GROUP BY product_id
) AS subquery ON s.product_id = subquery.product_id AND s.year = subquery.first_year;
