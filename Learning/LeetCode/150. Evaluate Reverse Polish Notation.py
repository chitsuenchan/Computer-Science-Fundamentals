"""
    Difficulty 2/10
    Beats 80% of submissions

    Stack question
    Got it relatively quickly with minor syntax errors and no help
    Understood conceptually what needs to be done
"""

from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        print("tokens: ", tokens)
        stack = deque()

        for char in tokens:
            if char == "*" and stack:
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num1) * int(num2)
                stack.append(result)
            elif char == "/" and stack:
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) / int(num1)
                stack.append(result)
            elif char == "+" and stack:
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num1) + int(num2)
                stack.append(result)
            elif char == "-" and stack:
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) - int(num1)
                stack.append(result)
            else:
                stack.append(char)

        return int(stack.pop())