#https://github.com/MrAsimZahid/LeetCode
#https://leetcode.com/problems/boats-to-save-people/
​
#Now lets speed optimize by reducing vaiabl names 
#
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        l: left
        r: right
        v: visits
        For better readablity visit last commit
        """
        people.sort()
        l = v = 0
        r = len(people) -1
        while r > l:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            v += 1
        if l == r:
            v += 1
        return v
