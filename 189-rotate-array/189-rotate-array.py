# mrasimzahid.github.io

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums
        nums[:] = nums[len_nums-k:] + nums[:len_nums-k]