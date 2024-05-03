"""
    Passes Test cases but not optimal solution.

    This is because we create subarrays in each for loop which is extra space complexity
    Also, we find the sum of each subarray inside the loop so it makes the time complexity 0(n^2)
"""

def pivotIndex(n) -> int:

    for i in range(len(n)):
        ls = n[:i]
        rs = n[i +1:]

        if sum(ls) == sum(rs):
            return i

    return -1

print(pivotIndex([1,7,3,6,5,6]))