"""
    Passes
    Beats 50%

    Difficulty 5/10 - Tried heap first but quickly knew to create tuples and sort that list

    Time Complexity: O(n log n)
    Space Complexity: O(n + k)
"""

import math

def kClosest(points, k):
    def distanceFromOrigin(coordinate):
        return math.sqrt((0 - coordinate[0]) ** 2 + (0 - coordinate[1]) ** 2)

    distances = []
    for coordinate in points:
        distance = distanceFromOrigin(coordinate)
        distances.append((coordinate, distance))


    sorted_distances = sorted(distances, key=lambda x: x[1])[:k]  # Sort by the second element of each tuple

    result = []
    for distance in sorted_distances:
        result.append(distance[0])

    return result

kClosest([[3, 3], [5, -1], [-2, 4]], 2)
# kClosest([[0,1],[1,0]], 2)
