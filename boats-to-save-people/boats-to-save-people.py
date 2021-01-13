#https://github.com/MrAsimZahid/LeetCode
#https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = visit = 0
        right = len(people) -1
        while right > left:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            visit += 1
        if left == right:
            visit += 1
        return visit
