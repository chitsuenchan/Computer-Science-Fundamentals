def countNegatives(grid):
    count = 0

    for i in range(0, len(grid)):

        for j in range(0, len(grid[i])):

            print(grid[i][j])
            if grid[i][j] < 0:
                count += 1
    return count

grid = [[5,1,0],[-5,-5,-5]]

print(countNegatives(grid))