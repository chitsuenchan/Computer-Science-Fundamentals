
# 8/12 Test cases passed
# Doesn't pass for test cases with large numbers

def sumXor(n):
    if n == 0:
        return 1
    else:
        count = 0
        while n:
            if n % 2 == 0:
                count += 1
            n >>= 1
        return 2 ** count


sumXor(1000000000000000)
