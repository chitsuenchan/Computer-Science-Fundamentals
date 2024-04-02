
# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150
# Hashmap, array
# T -> O(n)
# S -> O(n)

def twoSum(nums, target):

    hashmap = {}

    for i in range(len(nums)):
        print(hashmap)
        left_over = target - nums[i]
        print(left_over)
        if left_over in hashmap:
            print("FOUND")
            return [hashmap.get(left_over), i]

        hashmap[nums[i]] = i



print(twoSum([2,7,11,15], 9))