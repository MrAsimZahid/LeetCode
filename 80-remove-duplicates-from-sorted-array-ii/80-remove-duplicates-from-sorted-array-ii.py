# mrasimzahid.github.io

# Time: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_index = 1
        prev = nums[0]
        repeat_count = 1
        for index, current in enumerate(nums[1:]):
            if prev != current:
                prev = current
                repeat_count = 1
            else:
                repeat_count += 1
                
            if repeat_count <= 2:
                nums[len_index] = current
                len_index += 1
        return len_index