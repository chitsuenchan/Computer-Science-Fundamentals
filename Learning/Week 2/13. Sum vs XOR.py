
# 8/12 Test cases passed
# Doesn't pass for test cases with large numbers

def sumXor(n):
    print(n)

    count = 0

    for x in range(0, n + 1):
        print(x)
        if n + x == n ^ x:
            print("YES")
            count += 1

    return count



sumXor(1000000000000000)
