class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       return nums.index(max(nums))   
"""
        left_index, right_index = 0, len(nums) - 1
        while left_index <= right_index: 
            mid = left_index + (right_index - left_index) // 2; 
            
            if (mid-1<0 or nums[mid]>nums[mid-1]) and (mid+1>=len(nums) or nums[mid]>nums[mid+1]):
                return mid
            elif mid-1>=0 and nums[mid]<nums[mid-1]:
                # the opposite of the above "if" are these two "elif"
                right_index = mid - 1
            elif mid+1<len(nums) or nums[mid]<nums[mid+1]:
                left_index = mid + 1
        return left_index     
    """
