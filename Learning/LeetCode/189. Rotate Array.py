
# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
# Time complexity: 0(N*K)
# Not the optimal time complexity there is a better solution at 0(N)

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # Handle edge cases where k is greater than length of array
    k %= len(nums)

    # Perform rotation k times
    for _ in range(k):
        # Take out the last element
        last_element = nums.pop()
        # Insert it at the beginning
        nums.insert(0, last_element)