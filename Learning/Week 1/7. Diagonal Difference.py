

def diagonalDifference(arrays):

    # TL_BR
    i = 0
    j = len(arrays) - 1
    sum_TLBR = 0
    sum_TRBL = 0
    for array in arrays:
        sum_TLBR += array[i]
        i += 1

    for array in arrays:
        sum_TRBL += array[j]
        j -= 1


    # print(abs(sum_TLBR - sum_TRBL))
    return abs(sum_TLBR - sum_TLBR)



diagonalDifference([[1,2,3],[4,5,6],[9,8,9]])
diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]])







