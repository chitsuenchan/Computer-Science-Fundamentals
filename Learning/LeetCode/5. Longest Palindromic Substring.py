"""
    Passes
    Beats 10% on time

    Difficulty 4/10
    Solution is 0(n^3)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(word):
            return word == word[::-1]

        if len(s) == 1:
            return s[0]

        longest = ""

        for i in range(len(s)):
            left = i
            right = len(s)

            while not isPalindrome(s[left: right]) and left < right:
                right -= 1

            if isPalindrome(s[left:right]):
                word = "".join(s[left:right])
                if len(word) > len(longest):
                    longest = word

        return longest



