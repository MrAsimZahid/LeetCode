# from collections imoport deque, defaultdict

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # final_interval = []
        inter_interval = []
        index = 0
        intervals = sorted(intervals)
        while index < len(intervals) - 1:
            start, end = intervals[index], intervals[index+1]
            
            if start[0] > end[0] and start[0] > end[1]:
                intervals[index] = end
                intervals[index+1] = start
                
            elif start[0] > end[0]:
                element = [end[0],max(start[1],end[1])]
                intervals.pop(index)
                intervals[index] = element
        
                
            elif start[1] >= end[0]:
                element = [start[0], max(start[1],end[1])]
                intervals.pop(index)
                intervals[index] = element
                # final_interval.append(element)
            else:
                # final_interval.append(start)
                index += 1
        return intervals
            
        
#         for index in range(1, len(intervals)):
#             start, end = interval[index - 1], interval[index]
#             if start[1] >= end[0]:
#                 element = [start[0], end[1]]
#                 final_interval.append(element)
#             else:
#                 final_interval.append(start)
                
#                 deque([[1,3],[2,6],[8,10],[15,18]])



2