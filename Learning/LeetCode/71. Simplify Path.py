"""
    Didn't get this one at all
    Difficulty 8/10
"""

from collections import deque

def simplifyPath(path):
    stack = deque()
    stack.append("/")

    for i in range (1, len(path)):
        print("index is", i)
        print("char is", path[i])
        print("stack is", stack)

        if path[i] == "/" and path[i - 1] == "/":
            stack.pop()



        stack.append(path[i])


simplifyPath("/home/user//Documents/../../../usr/local/bin")