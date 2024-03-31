
# This solution transposes the grid to effectively sort columns as rows. This simplifies the sorting.

def gridChallenge(grid):

    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] < grid[i-1][j]:
                return "NO"

    return "YES"



# Example usage:
grid = [
    "ebacd",
    "fghij",
    "olmkn",
    "trpqs",
    "xywuv"
]
print(gridChallenge(grid))
