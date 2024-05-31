"""
    Got this solution in 5 minutes

    Beats 80%
"""

from collections import deque


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()

        for char in s:
            if char == ")" and stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return len(stack)