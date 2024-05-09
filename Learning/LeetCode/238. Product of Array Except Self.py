"""
    Complete fail

"""

def productExceptSelf(nums):

    result = []
    total_product = 1

    for num in nums:
        total_product *= num

    for i in range(len(nums)):
        left_slice = nums[:i]
        right_slice = nums[i + 1:]

        print("current i is", i)
        print(" left slice is", left_slice)
        print(" right slice is", right_slice)
        print("")

        product = total_product // nums[i]

        result.append(product)

    return result




print(productExceptSelf([1,2,3,4]))