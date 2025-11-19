class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = bin(n)[2:]
        rev_binary = reversed(binary)
        even, odd = 0, 0
        for index, val in enumerate(rev_binary):
            if val == "1":
                if index % 2:
                    odd += 1
                else:
                    even +=1
        return [even, odd]