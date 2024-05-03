def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return nums

    slow = 0

    for i in range(1, len(nums)):
        if nums[slow] == 0 and nums[i] != 0:
            nums[slow], nums[i] = nums[i], nums[slow]

        if nums[slow] != 0:
            slow += 1

moveZeroes([1,0,1])
moveZeroes([0,1,0,3,12])