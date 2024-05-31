"""
    On the right trtack conceptually and medium close with code
    But could not quite get some items such as:
        - Special edge cases
        - Adding a visited set
        - Incrementing the count at the end of each BFS
        - Declaring neighbour directions outside the BFS while loop and not inside
        - Initialisation of set is wrong
        - Initialisation of q could be better

    Difficulty 7/10

"""

from collections import deque

def shortestPathBinaryMatrix(grid):


    count = 0
    q = deque()
    q.append((0,0))
    end = (len(grid) - 1, len(grid[0]) - 1)

    while q:
        current = q.popleft()
        row = current[0]
        col = current[1]
        print((row, col))

        if current == end:
            return count

        neighbours_directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        for dr, dc in neighbours_directions:
            r = row + dr
            c = col + dc
            print(" ", (r, c))
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                print("     grid element is inbound", grid[r][c])
                if grid[r][c] == 0:
                    q.append((r,c))
                    print("     grid element is 0 so appending")
                    count += 1



print(shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
