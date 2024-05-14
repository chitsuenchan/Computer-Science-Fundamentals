"""
    Passed
    Beats 96% of submissions
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        first_product = nums[-2] * nums[-1]
        second_product = nums[0] * nums[1]

        return first_product - second_product