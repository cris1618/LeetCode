# Write your MySQL query statement below
SELECT class
FROM (
SELECT class, COUNT(class) AS counts
    FROM courses
    GROUP BY class
) AS counts
WHERE counts >= 5;