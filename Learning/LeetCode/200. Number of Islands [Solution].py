"""
    Utitlizes a BFS approach
        1. Creates a visited empty set which will store all of the visited coordinates
        2. Islands will initially be set to zero
        3. Loop through every coordinate in the grid
            3.1. if coordinate not seen already in visited AND the value is a 1 then proceed to BFS at 4.
        4. Start BFS on coordinate
            4.1. create an empty queue using the collections library
            4.2. Add the coordinate to the visited set
            4.3. Add the coordinate to the queue
            4.4. While there is still stuff in the queue we pop the first item and assign it to two variables row and col
            4.5. We have 4 directions in a 2D array which is up, down, right, left
            4.6. for each direction we will adjust the coordinate in question with the direction to go in
            4.7. If new row and col nearby in within the range of our len col and row AND its value is a 1 AND its not in visited then do 4.8
            4.8. Add this new neighbour to the queue and add it to visited set
        5. After BFS is complete we add +1 to islands count
        6. Return islands count

"""
import collections


def numIslands(grid):

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(row, col):
        q = collections.deque()
        visited.add((row, col))
        q.append((row, col))

        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1,0], [0,1],[0,-1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row,col) not in visited:
                bfs(row, col)
                islands += 1
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]

grid = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]

print(numIslands(grid))