"""
    Solution actually utilizes a min-heap

    The time complexity of the provided solution is primarily dominated by two operations:

        Calculating the distance for each point: This requires constant time O(1) for each point, so for n points, it's O(n).
        Building the heap: Inserting each element into the heap takes O(log k) time, and we do this for each of the n points. So, the total time complexity for building the heap is O(n log k).
        Therefore, the overall time complexity is O(n log k), where n is the number of points and k is the value of k.

    For the space complexity:

        We use a heap to store the distances and points, which would take O(k) space.
        Apart from the heap, we don't use any additional space that scales with the input size.
        So, the overall space complexity is O(k).
"""

import heapq


def kClosest(points, k):
    heap = []

    for point in points:
        distance = point[0] ** 2 + point[1] ** 2

        # When pushing onto the heap it looks at the first element inside the tuple to determine what is the minimum
        heapq.heappush(heap, (distance, point))

    k_closest = []

    # We do k amount of loops appending to the k_closest the smallest all the way to the largest but only up to k
    for _ in range(k):
        k_closest.append(heapq.heappop(heap)[1])

    return k_closest


# Example usage:
points = [[1, 3], [-2, 2], [5, -1], [0, 0]]
k = 2
print(kClosest(points, k))  # Output will be [[0, 0], [1, 3]]
