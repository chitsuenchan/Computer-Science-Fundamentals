"""
    Passes all test cases
"""


def findDifference(nums1, nums2):

    s1 = set(nums1)
    s2 = set(nums2)

    results = []

    s1_dif = list(s1.difference(s2))
    s2_dif = list(s2.difference(s1))

    results.append(s1_dif)
    results.append(s2_dif)

    return results


nums1 = [1,2,3]
nums2 = [2,4,6]

s1 = set(nums1)
s2 = set(nums2)



print(list(s1.difference(s2)))

print(findDifference(nums1, nums2))


