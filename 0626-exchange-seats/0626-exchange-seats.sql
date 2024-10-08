# Write your MySQL query statement below
SELECT 
    CASE
        WHEN MOD(id, 2) = 1 AND id + 1 <= (SELECT MAX(id) FROM seat) THEN id + 1
        WHEN MOD(id, 2) = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM seat
ORDER BY id;
