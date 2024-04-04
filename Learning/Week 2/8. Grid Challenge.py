
# PASS 11/12 test cases

# def gridChallenge(grid):
#     print(grid)
#     sorted_grid = []
#
#     if len(sorted_grid) == 1:
#         return "YES"
#
#     for row in grid:
#         sorted_row = "".join(sorted(row))
#         sorted_grid.append(sorted_row)
#
#
#     for row in sorted_grid:
#         print(row)
#
#
#     for i in range(0, len(sorted_grid)-1):
#
#         column = []
#
#         print("we are on letter", sorted_grid[0][i])
#
#         for j in range(0, len(sorted_grid)):
#             column.append(sorted_grid[j][i])
#
#         print(column)
#         sorted_column = sorted(column)
#         print(column)
#         print(sorted_column)
#         if column != sorted_column:
#             return "NO"
#
#     return "YES"


def gridChallenge(grid):
    if len(grid) == 1:
        return "YES"

    for row in grid:
        for i in range(1, len(row)):
            if grid[row][i] < grid[row][i -1]:
                return "NO"

    return "YES"





gridChallenge(['l'])
