# mrasimzahid.github.io

# Time: O(n)
# Space: O(n)

# Technique: negative dictionary 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot_sum = 0
        sums = 0
        nums_dict = dict()
        nums_dict[0] = 1
        arr_len = len(nums)
        for index in range(arr_len):
            sums += nums[index]
            tot_sum += nums_dict.get(sums - k, 0)
            nums_dict[sums] = nums_dict.get(sums, 0) + 1
        
        return tot_sum
    
        # Time: O(n^2)
        # Space: O(1)
        # Technique: Sliding Window    

        # for win_len in range(arr_len):
        #     for i in range(arr_len):
        #         res = nums[i:win_len+1]
        #         if sum(res) == k and res != []:
        #             tot_sum += 1
        # return tot_sum
        