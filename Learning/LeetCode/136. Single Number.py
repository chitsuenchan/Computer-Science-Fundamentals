"""
    Passes the test but wrong implementation

    Time complexity is 0(n)
    Space complexity is 0(n)
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1


        for item in hashmap.items():
            if item[1] == 1:
                return item[0]