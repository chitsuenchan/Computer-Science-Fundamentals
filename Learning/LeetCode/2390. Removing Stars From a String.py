
"""
    Passed in one try in 5 minutes
"""


def removeStars(s):

    stack = []

    for char in s:
        stack.append(char)

        if char == "*":
            stack.pop()
            stack.pop()

    return "".join(stack)

removeStars("leet**cod*e")