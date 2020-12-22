#https://leetcode.com/problems/reverse-bits/
#https://github.com/MrAsimZahid
class Solution:
    def reverseBits(self, n: int) -> int:
        return int((bin(n)[2:].zfill(32))[::-1], 2)
    """
    unsigned int : 32 char
    bin() : convert number into binary, slicing is remove 0b on left side.
    zfill: returns a copy of the string with '0' characters padded to the left.
    [::-1] : reverse the string
    int(num, 2): convert into int with binary
    """
