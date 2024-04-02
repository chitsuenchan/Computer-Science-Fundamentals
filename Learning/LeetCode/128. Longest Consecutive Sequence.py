
def containsNearbyDuplicate(nums, k):

    for row in range(len(nums)):
        for col in range(len(nums)):
            if row != col:
                if nums[col] == nums[row]:
                    if abs(row - col) <= k:
                        return True
    return False


print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))


