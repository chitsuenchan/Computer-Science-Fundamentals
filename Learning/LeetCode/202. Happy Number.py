
def squared_sum_of_digits(num):
    s = str(num)

    total = 0
    for digit in s:
        total += int(digit) ** 2

    return total

def isHappy(n):

    answers = {}

    while n != 1:
        n = squared_sum_of_digits(n)

        if n in answers:
            return False

        answers[n] = True

    return True






# isHappy(19)
print(isHappy(89))