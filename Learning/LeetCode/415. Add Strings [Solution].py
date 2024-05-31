"""
    Didn't get this problem

    Need to treat it as you would when you add together two numbers in non-calculator math
"""

def addStrings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1

    carry = 0
    result = []

    while i >= 0 or j >= 0:
        current_i = int(num1[i]) if i >= 0 else 0
        current_j = int(num2[j]) if j >= 0 else 0

        current_sum = carry + current_i + current_j

        result.append(str(current_sum % 10))

        carry = current_sum // 10

        i -= 1
        j -= 1

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])


print(addStrings("456", "77"))
