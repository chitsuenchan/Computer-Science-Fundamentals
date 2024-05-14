"""
    Passes
    Beats 90%
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if stack:
                    if char == "}" and stack[-1] == "{":
                        stack.pop()
                    elif char == ")" and stack[-1] == "(":
                        stack.pop()
                    elif char == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if stack:
            return False

        return True



