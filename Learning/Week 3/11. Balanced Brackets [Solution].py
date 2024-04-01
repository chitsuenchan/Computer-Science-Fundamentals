

def isBalanced(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        elif bracket in brackets.keys():
            if not stack or brackets[bracket] != stack.pop():
                return "NO"
        else:
            return "NO"

    return "YES" if not stack else "NO"



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
