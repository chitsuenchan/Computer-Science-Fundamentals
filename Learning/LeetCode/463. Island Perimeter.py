"""
    Passed
    Beats 70%
    Difficulty 5/10 - Got it in about 20 minutes
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    square_p = 4

                    # Execute if top is there
                    if not (i - 1 < 0) and grid[i - 1][j] == 1:
                        square_p -= 1

                    # Execute if bottom is there
                    if not (i + 1 > len(grid) - 1) and grid[i + 1][j] == 1:
                        square_p -= 1

                    # Execute if left is there
                    if not (j - 1 < 0) and grid[i][j - 1] == 1:
                        square_p -= 1

                    # Execute if left is there
                    if not (j + 1 > len(grid[0]) - 1) and grid[i][j + 1] == 1:
                        square_p -= 1

                    result += square_p
        return result