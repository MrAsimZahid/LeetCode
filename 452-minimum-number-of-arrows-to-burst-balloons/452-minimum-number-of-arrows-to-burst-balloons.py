# mrasimzahid.github.io

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[1])
        # return points
        count = 0
        while points:
            flag = points[0][1]
            # return flag
            while flag >= points[0][0]:
                points.pop(0)
                if points == []:
                    break
            count += 1
        return count
    