"""
    Didn't get the correct solution.

    Was on the right track on using two-pointers but chose to start the two pointers at the beginning.
    Instead the correct solution was to have a pointer at the start and end and work towards the middle.
    This is because the list is sorted in descending order

    Difficulty 7/10
"""

def twoSum(nums, target):

    slow, fast = 0, 0

    while fast < len(nums):

        slow_n = nums[slow]
        fast_n = nums[fast]

        if slow_n + fast_n == target and slow != fast:
            return [slow + 1, fast + 1]

        if slow_n + fast_n < target or slow == fast:
            fast += 1
        else:
            slow += 1

    return -1




# twoSum([1,2,7,11,15,20], 17)
# twoSum([0,0,3,4], 0)
print(twoSum([5,25,75], 100))