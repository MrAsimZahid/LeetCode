# mrasimzahid.github.io

# Time: O(log(n))
# Space: O(1)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        start = 0
        end = len(people)- 1
        while start <= end:
            if people[start] + people[end] <= limit:
                start +=1
                end -= 1
            else:
                end -= 1
            boats += 1
        return boats