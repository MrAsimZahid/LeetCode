#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
#https://github.com/MrAsimZahid
class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num/2
                steps += 1
            if num % 2 != 0:
                num -= 1
                steps += 1
        return steps
