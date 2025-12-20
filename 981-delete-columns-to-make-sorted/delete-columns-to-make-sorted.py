class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        del_col = 0
        cols = len(strs[0])
        for i in range(cols):
            start = 0
            for index, val in enumerate(strs):
                ascii_val = ord(val[i])
                if start > ascii_val:
                    del_col += 1
                    break
                else:
                    start = ascii_val

        return del_col

