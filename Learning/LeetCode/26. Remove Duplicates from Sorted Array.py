
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):

    comparison_pointer = 0

    for i in range(0, len(nums)):
        if nums[i] != nums[comparison_pointer]:
            comparison_pointer += 1
            nums[i], nums[comparison_pointer] = nums[comparison_pointer], nums[i]

    return nums


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
