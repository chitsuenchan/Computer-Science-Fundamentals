
def containsNearbyDuplicate(nums, k):

    nums_dict = {}

    for i, num in enumerate(nums):
        print(num)
        if num in nums_dict and i - nums_dict[num] <= k:
            return True

    return False

# print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
# print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))


