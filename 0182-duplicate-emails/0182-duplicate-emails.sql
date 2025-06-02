# Write your MySQL query statement below
SELECT Email AS email FROM Person
GROUP BY email HAVING 
COUNT(email)>1;