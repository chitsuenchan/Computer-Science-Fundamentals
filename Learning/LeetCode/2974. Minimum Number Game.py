
"""
    Passes all tests
    96% beats submission very fast

    Time complexity O(nlogn)
        This is because of sorting the list

    Space compleixty 0(n)
        This is because the arr maximum size can only be the size of the input
"""

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        arr = []

        nums.sort(reverse=True)

        while nums:
            alice_num = nums.pop()
            ben_num = nums.pop()

            arr.append(ben_num)
            arr.append(alice_num)

        return arr
