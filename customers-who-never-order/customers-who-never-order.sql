#https://leetcode.com/problems/customers-who-never-order/
#https://github.com/MrAsimZahid
# Write your MySQL query statement below
SELECT Name AS Customers FROM Customers LEFT JOIN Orders ON Customers.Id = Orders.CustomerId WHERE Orders.CustomerId IS NULL;
