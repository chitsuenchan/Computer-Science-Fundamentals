"""
    Could not get the solution.

    Need to use two pointers

    Difficulty 10/10
"""


def threeSum(nums):
    # Sort the array
    nums.sort()
    result = []

    # Iterate through the array, considering each number as a potential first element of a triplet
    for i in range(len(nums) - 2):
        # Skip the same element to avoid duplicates in the result
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two pointers to find the other two elements of the triplet
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip the same elements to avoid duplicates in the result
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

print(threeSum([-1,0,1,2,-1,-4]))