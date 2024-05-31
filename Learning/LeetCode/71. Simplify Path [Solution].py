"""

"""

from collections import deque

def simplifyPath(path):
    stack = deque()
    current_word = ""

    for char in path + "/":
        if char == "/":
            if current_word == "..":
                stack.pop()
            elif current_word != "" and current_word != ".":
                stack.append(current_word)
            current_word = ""
        else:
            current_word += char

    return "/" + "/".join(stack)




print(simplifyPath("/home/user//Documents/../../../usr/local/bin"))