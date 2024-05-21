"""
    Passed

    Uses DFS to get the perimeter for every single cell\
    Actually slower than my solution
"""


def islandPerimeter(grid):

    visited = set()

    def dfs(i, j):
        # 1. Base case - If hits boundary or water
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 1

        # 2. Base case - if it hits a seen node already
        if (i, j) in visited:
            return 0

        # Mark cell as visited
        visited.add((i, j))

        # Recursive steps
        perimeter = dfs(i + 1, j)
        perimeter += dfs(i - 1, j)
        perimeter += dfs(i, j + 1)
        perimeter += dfs(i, j - 1)

        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Check if it's land
                return dfs(i, j)  # Start DFS from this land cell

grid = [
    [0,1,0,0,0],
    [1,1,1,0,0],
    [0,1,0,0,0],
    [1,1,0,0,0]
]

print(islandPerimeter(grid))