class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        str_val, res = "", []
        for index, num in enumerate(nums):
            str_val += str(num)
            res.append(int(str_val, 2) % 5 == 0)
        return res

