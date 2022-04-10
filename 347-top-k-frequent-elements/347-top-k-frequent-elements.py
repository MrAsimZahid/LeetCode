# mrasimzahid.github.io

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_count = collections.Counter(nums)
        res_list = res_count.most_common(k)
        return list(zip(*res_list))[0]
        