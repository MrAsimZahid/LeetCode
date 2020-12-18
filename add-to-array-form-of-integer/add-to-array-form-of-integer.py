#https://leetcode.com/problems/add-to-array-form-of-integer/
#https://github.com/MrAsimZahid
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        #Solution 1
        return list(str(int("".join(map(str, A))) + K))
        """
        #Solution 2
        str_int = ""
        for i in range(len(A)):
            str_int += str(A[i])
        x = str(int(str_int) + K)
        arr = []
        for i, v in enumerate(x):
            arr.append(v)
        return arr
    """
