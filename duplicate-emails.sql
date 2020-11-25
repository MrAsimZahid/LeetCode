# Write your MySQL query statement below
SELECT Email from Person GROUP BY Email HAVING COUNT(Email) > 1;
​
