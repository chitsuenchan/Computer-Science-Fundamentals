
def transpose(matrix):
    new_matrix = []
    for i in range(0, len(matrix)):
        row = []
        for j in range (0, len(matrix[i])):
            print(matrix[j][i])
            row.append(matrix[j][i])

        new_matrix.append(row)

    return new_matrix




matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(transpose(matrix))
