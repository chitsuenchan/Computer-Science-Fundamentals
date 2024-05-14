
"""
    Pass all tests
    Only beats 5% of submissions

    Time complexity: 0(n^2)
    Space complexity: 0(n)
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        blue_idx = 0
        result = ""

        while blue_idx < len(s):
            for i in range(len(s)):
                if blue_idx == indices[i]:
                    result += s[i]
                    blue_idx += 1
        return result