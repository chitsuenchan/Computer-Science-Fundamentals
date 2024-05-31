"""
    Got this question after 15 minutes of coding.

    Mind went blank initially and had to rest a bit before returning.
    Solved this question before but forgot the solution.

    Difficulty 4/10
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        strs.sort(key=len)
        shortest = strs[0]
        pointer = 0
        prefix = ""

        while pointer < len(shortest):
            all_match = True
            for word in strs:
                if word[pointer] != shortest[pointer]:
                    all_match = False

            if all_match:
                prefix += word[pointer]
            else:
                break

            pointer += 1

        return prefix
