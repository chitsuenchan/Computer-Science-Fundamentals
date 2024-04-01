"""

    20/20 test cases passed
"""

def isBalanced(s):
    lst = list(s)
    print(lst)

    stack = []

    for bracket in lst:
        print(stack)
        print(bracket)
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.append(bracket)


        if len(stack) == 0:
            return "NO"

        if bracket == ")":
            compare_bracket = stack.pop()
            if compare_bracket != "(":
                return "NO"

        if bracket == "}":
            compare_bracket = stack.pop()
            if compare_bracket != "{":
                return "NO"

        if bracket == "]":
            compare_bracket = stack.pop()
            if compare_bracket != "[":
                return "NO"

    if len(stack) != 0:
        return "NO"

    return "YES"




print(isBalanced("{{[()]}[][]()}"))
# print(isBalanced("{(([])[])[]}[]"))
# print(isBalanced("{[(])}"))
# print(isBalanced("][(]}})("))
# print(isBalanced("{[()]}"))
# print(isBalanced("{[()]}"))




# YES
# {(([])[])[]}

# YES
# {(([])[])[]}[]

# YES
# {[()]}

# Don't know
# {[[(({[[(({[[(({[[(({[[(({[[(({[[(({[[(({[[(({[[(({[[(({[[(())]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}))]]}}
