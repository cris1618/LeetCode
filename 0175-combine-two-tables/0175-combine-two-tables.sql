# Write your MySQL query statement below
SELECT 
    p.firstName, 
    p.lastName,
    CASE 
        WHEN a.city IS NULL THEN null 
        ELSE a.city 
    END AS city,
    CASE 
        WHEN a.state IS NULL THEN null 
        ELSE a.state 
    END AS state
FROM 
    Person AS p
LEFT JOIN 
    Address AS a 
ON 
    p.personId = a.personId;




