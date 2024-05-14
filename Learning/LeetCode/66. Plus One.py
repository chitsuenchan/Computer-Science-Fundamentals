"""
    Passes
    Beats 80%

    Difficulty 3/10
    Must know how to convert types
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_int = int(''.join(map(str, digits)))
        digits_int += 1
        digits_str = str(digits_int)
        digits_list = []

        for char in digits_str:
            digits_list.append(int(char))

        return digits_list