def spiralOrder(matrix):
    seen = set()

    for row in matrix:
        print(row)

    direction = "right"
    row = 0
    col = 0
    row_size = len(matrix)
    col_size = len(matrix[0])
    current = (row, col)

    if direction == "right":
        while col < col_size:
            current = (row, col)
            element = matrix[0][col]
            print(f"Coordinate: {current}. Element: {element}")
            seen.add(current)
            col += 1
        direction = "down"
        col -= 1
    print("")

    if direction == "down":
        while row < row_size:
            current = (row, col)
            element = matrix[row][col]
            print(f"Coordinate: {current}. Element: {element}")
            seen.add(current)
            row += 1
        direction = "left"
        row -= 1
    print("")

    if direction == "left":
        while col >= 0:
            current = (row, col)
            element = matrix[row][col]
            print(f"Coordinate: {current}. Element: {element}")
            seen.add(current)
            col -= 1
        direction = "up"
        col += 1
    print("")

    if direction == "up":
        while row >= 0 and (row, col):
            current = (row, col)
            element = matrix[row][col]
            print(f"Coordinate: {current}. Element: {element}")
            seen.add(current)
            row -= 1
        direction = "right"
        print("")

    print(current)
    print(seen)

    direction = "down"






    return []


print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))