# mrasimzahid.github.io

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num_list = nums
        self.k = k 

    def add(self, val: int) -> int:
        self.num_list.append(val)
        self.num_list.sort()
        return self.num_list[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)