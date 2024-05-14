"""
    Passed
    Beats 22% of submissions
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0

        if len(points) == 1:
            return 0

        for i in range(1, len(points)):
            x = points[i][0]
            y = points[i][1]
            prev_x = points[ i -1][0]
            prev_y = points[ i -1][1]

            difference_x = abs( x -prev_x)
            difference_y = abs( y -prev_y)
            total += max(difference_x, difference_y)

        return total
