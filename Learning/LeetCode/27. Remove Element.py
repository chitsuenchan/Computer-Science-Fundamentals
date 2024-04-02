
# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def removeElement(nums, val):
    back_pointer = len(nums) - 1

    print("value is:", val)


    for i in range(len(nums)):

        print("Number we are on:", nums[i])
        print(" lst is:", nums)
        print(" back pointer", back_pointer)

        while nums[back_pointer] == val and back_pointer >= i:
            back_pointer -= 1

        if i >= back_pointer:
            break
        print(" back pointer", back_pointer)
        print(" back pointe number:", nums[back_pointer])
        if nums[i] == val:
            nums[i], nums[back_pointer] = nums[back_pointer], nums[i]
            back_pointer -= 1

    print("Final array", nums)
    return back_pointer + 1


nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))
