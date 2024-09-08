# Write your MySQL query statement below
SELECT DISTINCT p.product_id, p.product_name
FROM sales AS s
LEFT JOIN product AS p 
ON p.product_id = s.product_id
GROUP BY(product_id)
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31';