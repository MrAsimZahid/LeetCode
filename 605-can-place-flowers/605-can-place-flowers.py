# mrasimzahid.github.io

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return sum((len(zeros) - 1) // 2 for zeros in ''.join(map(str, [0] + flowerbed + [0])).split('1')) >= n