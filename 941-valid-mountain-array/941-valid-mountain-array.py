# mrasimzahid.github.io

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <=2 or arr[0] >= arr[1]:
            return False
        flag = True
        for i in range(1, len(arr)):
            if flag:
                if arr[i] <= arr[i-1]:
                    flag = False
            if not flag:
                if arr[i] >= arr[i-1]:
                    return False
        return not flag