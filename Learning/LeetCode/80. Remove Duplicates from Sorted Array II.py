

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

def removeDuplicates(nums):

    if len(nums) <= 2:
        return len(nums)

    comparison_pointer = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[i] = nums[comparison_pointer]
            i += 1
    return i

print(removeDuplicates([0,0,1,1,1,1,1,1,2,2,3,3,4]))