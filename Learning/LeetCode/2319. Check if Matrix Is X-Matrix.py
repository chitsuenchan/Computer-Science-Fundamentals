"""
    Passes
    Beats 5% of submissions
"""
def checkXMatrix(grid):

    up = 0
    down = len(grid[0]) -1
    diagonal_indexes = []
    for i in range(len(grid[0])):
        diagonal_indexes.append((i,up))
        diagonal_indexes.append((i,down))
        up += 1
        down -= 1


    print(diagonal_indexes)

    for i in range(len(grid)):
        print(grid[i])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print("current i and j is", (i,j))
            print("current value is", grid[i][j])

            if (i,j) in diagonal_indexes:
                print(" in diagnol indexes")
                if grid[i][j] == 0:
                    return False
            else:
                print(" NOT in  diagnol indexes")
                if grid[i][j] != 0:
                    return False
            print("")

    return True


print(checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
print(checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]))