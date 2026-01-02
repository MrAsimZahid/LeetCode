class Solution:
    def maxPower(self, s: str) -> int:
        consecutive = 0
        max_cons = 0
        prev = ""
        for index, val in enumerate(s):
            if val == prev:
                consecutive += 1
                max_cons = max(max_cons, consecutive)
            else:
                consecutive = 1
                prev = val
        return max(max_cons, consecutive)

