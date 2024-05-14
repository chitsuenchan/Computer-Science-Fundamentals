"""
    Passes
    Beats 38%
"""


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0, 0]
        first = 0
        second = 0
        for i in range(len(nums1)):
            if i < len(nums1) and nums1[i] in nums2:
                first += 1

        result[0] = first

        for i in range(len(nums2)):
            if i < len(nums2) and nums2[i] in nums1:
                second += 1

        result[1] = second

        return result