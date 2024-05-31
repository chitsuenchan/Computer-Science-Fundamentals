"""
    On the right trtack conceptually and medium close with code
    But could not quite get some items such as:
        - Special edge cases
        - Adding a visited set
        - Incrementing the count at the end of each BFS
        - Declaring neighbour directions outside the BFS while loop and not inside
        -

    Difficulty 7/10

"""

from collections import deque

def shortestPathBinaryMatrix(grid):

    # Edge cases
    #   - no grid
    #   - start is not a zero
    #   - end is not a zero
    if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
        return -1

    n = len(grid)
    q = deque([(0, 0)])
    visited = set([(0,0)])
    count = 1
    neighbours_directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    while q:
        for _ in range(len(q)):
            row, col = q.popleft()

            if (row, col) == (len(grid) - 1, len(grid) -1):
                return count

            for dr, dc in neighbours_directions:
                r, c = row + dr, col + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0 and (r, c) not in visited:
                    q.append((r,c))
                    visited.add((r, c))
        count += 1

    return -1



print(shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
