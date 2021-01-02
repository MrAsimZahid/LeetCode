#https://leetcode.com/problems/big-countries/
#https://github.com/MrAsimZahid
# Write your MySQL query statement below
SELECT name, population, area FROM world WHERE world.area > 3000000 OR world.population > 25000000;
