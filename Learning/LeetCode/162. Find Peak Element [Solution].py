
def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2

        # Getting right mid
        left_rightSide = mid + 1
        right_rightSide = right

        mid_rightSide = (left_rightSide + right_rightSide) // 2

        # Getting left mid
        left_leftSide = left
        left_rightSide = mid - 1

        mid_leftSide = (left_leftSide + left_rightSide) // 2

        # If right side is higher
        if nums[mid_leftSide] < nums[mid] < nums[mid_rightSide]:
            # print(" Middle right element is largest")
            left = mid + 1

        # If left side is higher
        elif nums[mid_leftSide] > nums[mid] > nums[mid_rightSide]:
            # print(" Middle left element is largest")
            right = mid - 1

        elif nums[mid_leftSide] < nums[mid] and nums[left] < nums[mid]:
            left = mid + 1

        elif nums[mid_rightSide] < nums[mid] and nums[right] < nums[mid]:
            right = mid - 1

    return mid


print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
