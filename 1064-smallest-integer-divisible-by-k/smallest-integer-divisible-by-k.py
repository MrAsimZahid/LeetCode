class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = "1"
        reminder = 1
        for index in range(k):
            if index == 0:
                reminder = reminder % k
            else:
                reminder = (reminder * 10 + 1) % k
            if reminder == 0:
                return len(n) 
            n += "1"
        return -1

