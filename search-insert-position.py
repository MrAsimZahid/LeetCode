#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target)
        """
        if target == 0:
            return 0
        elif(nums[len(nums)-1] < target):
            return len(nums)
        else:
            return nums.index(target)
            #x = str(nums)
            #return x.find(str(target))
            """
        """
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) // 2
            if (nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        if left == len(nums):
            return left
        else:
            return left
            """
