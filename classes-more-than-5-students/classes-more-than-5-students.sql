#https://leetcode.com/problems/classes-more-than-5-students/
#https://github.com/MrAsimZahid
# Write your MySQL query statement below
SELECT class FROM courses GROUP BY class HAVING COUNT(DISTINCT student) >= 5;
