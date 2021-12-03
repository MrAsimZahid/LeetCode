class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev_digits = digits[::-1]
        digi_len = len(rev_digits)
        for each in range(digi_len):
            result = rev_digits[each] + 1
            if result < 10:
                rev_digits[each] = result
                break
            if result > 9:
                rev_digits[each] = 0
                if (digi_len - 1) == each:
                    rev_digits.append(1)
        return rev_digits[::-1]