"""
    Passes
    Beats 10% of users
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            idx = 2
            prev = [1, 1]

            while idx < rowIndex + 1:
                new = []
                new.append(1)

                for i in range(0, len(prev) - 1):
                    new.append(sum(prev[i:i + 2]))
                new.append(1)
                prev = new
                idx += 1
            return prev