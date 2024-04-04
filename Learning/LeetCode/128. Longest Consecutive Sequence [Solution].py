
def longestConsecutive(nums):

    num_dict = {}
    max_length = 0

    for num in nums:
        if num not in num_dict:
            left = num_dict.get(num - 1, 0)
            right = num_dict.get(num + 1, 0)
            length = left + right + 1

            num_dict[num] = length
            num_dict[num - left] = length
            num_dict[num + right] = length

            max_length = max(max_length, length)

    return max_length


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))


