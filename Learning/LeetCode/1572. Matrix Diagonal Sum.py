
def diagonalSum(mat):

    index = 0
    j = 0
    topleft_to_bottomright = 0
    topright_to_bottomleft = 0

    for i in range(len(mat[0])):
        topleft_to_bottomright += mat[i][j]
        j += 1

    j = 0
    for i in range(len(mat[0]) - 1, -1, -1):
        topright_to_bottomleft += mat[i][j]
        j += 1

    return topleft_to_bottomright + topright_to_bottomleft








mat = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]


mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))

