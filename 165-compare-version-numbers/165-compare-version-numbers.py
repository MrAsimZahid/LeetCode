# mrasimzahid.github.io

# Time: O(n)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        v1_len = len(v1)
        v2_len = len(v2)
        diff = abs(v1_len - v2_len)
        for each in range(diff):
            if v1_len > v2_len:
                v2.append("0")
            else:
                v1.append("0")
        for index in range(len(v1)):
            v1_i = int(v1[index])
            v2_i = int(v2[index])
            if v1_i < v2_i:
                return -1
            elif v1_i > v2_i:
                return 1
            else:
                res = 0
        return res