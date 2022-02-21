# mrasimzahid.github.io


# Time: O(n)
# Space: O(unique n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_max = {}
        for each in nums:
            if each in count_max:
                count_max[each] = count_max[each] + 1
            else:
                count_max[each] = 1
        max_val = 0
        _key = 0
        for each in count_max:
            temp = count_max.get(each)
            if max_val < temp:
                max_val = temp
                _key = each
        return _key