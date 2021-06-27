class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums): 
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i