"""
    Passes
    Beats 60% of users

    Difficulty 5/10 - Got it in about 30 minutes after waking up. Pretty much the optimal solution.
"""

from collections import deque

def minRemoveToMakeValid(s):
    stack = deque()

    for i, char in enumerate(s):
        print("character", char)
        print("stack is", stack)

        if char == "(":
            stack.append((char,i))

        elif char == ")":

            if stack:
                top = stack[-1]
                print("top of stack is:", top)

                if top[0] == "(":
                    stack.pop()
                    print("popped off (")
                else:
                    stack.append((char, i))
            else:
                stack.append((char, i))

        print("")


    s_list = list(s)
    print(s_list)

    while stack:
        top = stack.pop()
        s_list.pop(top[1])

    print(s_list)
    return "".join(s_list)


print(minRemoveToMakeValid("lee(t(c)o)de)"))