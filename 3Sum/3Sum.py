class Solution:
    """
    Approch:
    Hold one index and apply twoSum method.
    note equation:
    partial_sum = sum - value
    Now send partial_sum into twoSum algo.

    Complexity:  O(N^2)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        for outer_index in range(0, len(nums)):
            partial = sum - nums[outer_index]
            for inner_index in range(outer_index, len(nums)):
                difference = partial - nums[inner_index]
                if difference in hashmap:
                    # return all three indices 
                    return [nums[outer_index], hashmap[difference], inner_index]
                hashmap[nums[inner_index]] = inner_index