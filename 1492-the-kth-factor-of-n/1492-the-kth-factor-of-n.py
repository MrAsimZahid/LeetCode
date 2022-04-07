# mrasimzahid.github.io

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)

        if len(factors) >= k:
            return factors[k-1]
        else:
            return -1