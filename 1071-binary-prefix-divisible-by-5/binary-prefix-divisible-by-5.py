class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        nums = list(map(str, nums))
        for index, num in enumerate(nums):
            str_val =  "".join(nums[:index+1])
            val = int(str_val, 2)
            if val % 5:
                res.append(False)
            else:
                res.append(True) 
        return res

