"""
    Pass
    Beats 88%

    Difficulty 6/10 - needed help to sort the inner arrays by index 0

    Time: O(n log n)
    Space: 0(n)

    Same time and space as optimal solution
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        sorted_lst = sorted(intervals, key=lambda x: x[0])

        merged_lst = []
        for interval in sorted_lst:
            if not merged_lst:
                merged_lst.append(interval)

            elif interval[0] <= merged_lst[-1][1]:

                if interval[1] > merged_lst[-1][1]:
                    merged_lst[-1][1] = interval[1]
            else:
                merged_lst.append(interval)

        return merged_lst