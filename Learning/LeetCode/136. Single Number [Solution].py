"""
    Passes the test.

    Uses XOR to cancel out duplicates and leave only a single number

    Time complexity is 0(n)
    Space complexity is 0(1)

    Example:

    1. Initialization:
        We initialize result to 0.
    2. XOR Operation:
        We iterate through the array. Initially, result is 0.
            result ^= 4 -> result = 4
            result ^= 1 -> result = 4 ^ 1 = 5
            result ^= 2 -> result = 5 ^ 2 = 7
            result ^= 1 -> result = 7 ^ 1 = 6
            result ^= 2 -> result = 6 ^ 2 = 4
    3. Return Result:
        We return the value of result, which is 4.
"""

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4