"""
    Passed all tests and fast
"""

def leftRightDifference(nums):
    total = sum(nums)
    left_sum = 0
    result = []

    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]

        difference = abs(left_sum - right_sum)
        result.append(difference)
        left_sum += nums[i]

    return result