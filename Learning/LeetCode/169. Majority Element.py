
# My solution

def majorityElement(nums):
    dict = {}

    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    majority_element = None
    count = 0
    for item in dict.items():
        if item[1] > count:
            majority_element = item[0]
            count = item[1]
    return majority_element




nums = [3,3,4]
print(majorityElement(nums))