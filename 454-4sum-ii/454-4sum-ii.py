# mrasimzahid.github.io

# Time: O(n^2)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        num = collections.Counter(a+b for a in nums1 for b in nums2)
        return sum(num[-c-d] for c in nums3 for d in nums4)
    
        # num = nums1 + nums2 + nums3 + nums4
        # comb = [sum(each) for each in permutations(num, 4)]
        # comb = Counter(comb)
        # return comb
        # if len(nums1) % 2 == 0:
        #     res = (comb[0]-1)/4
        # else:
        #     res = ((comb[0]+1)/4) * 2
        # return res
    # [list(zip(each_permutation, list2)) for each_permutation in itertools.permutations(list1, len(list2))]
