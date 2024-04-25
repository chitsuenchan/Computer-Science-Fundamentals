


def repeatedString(s, n):

    count = 0

    for letter in s:
        if letter == 'a':
            count += 1

    d_result = n // len(s)
    d_remainder = n % len(s)

    result = d_result * count

    for letter in s[:d_remainder]:
        if letter == 'a':
            result += 1

    return result





# repeatedString('abcac', 10)


print(repeatedString('aaa', 16))