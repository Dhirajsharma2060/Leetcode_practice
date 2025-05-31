# Write your MySQL query statement below
#SELF.join concept used here matlab hi same table to e1 and e2 banake likna hai
SELECT e1.name AS Employee FROM Employee e1 
INNER JOIN Employee e2 ON e1.managerId=e2.id
WHERE e1.salary>e2.salary;
