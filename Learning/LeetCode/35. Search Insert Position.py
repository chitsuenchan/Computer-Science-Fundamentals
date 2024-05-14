"""
    Passes 43/65 tests

    difficulty rating 6/10
"""
def searchInsert(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        print("left", left)
        print("right", right)
        print("left boundary:", nums[left])
        print("right boundary:", nums[right])
        print("array:", nums[left:right +1])
        mid = (left + right) // 2
        print("middle", mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        print("")

    return mid + 1


# print(searchInsert([1,3,5,6],5))
# print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3],2))
