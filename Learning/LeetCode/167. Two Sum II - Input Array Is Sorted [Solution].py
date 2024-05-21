"""
    Beats 80% of users

"""

def twoSum(nums, target):

    left, right = 0, len(nums) - 1

    while left < right:

        slow_n = nums[left]
        fast_n = nums[right]

        if slow_n + fast_n == target and left != right:
            return [left + 1, right + 1]

        if slow_n + fast_n < target:
            left += 1
        else:
            right -= 1





# twoSum([1,2,7,11,15,20], 17)
# twoSum([0,0,3,4], 0)
print(twoSum([5,25,75], 100))