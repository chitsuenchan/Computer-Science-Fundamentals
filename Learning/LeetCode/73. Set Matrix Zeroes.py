"""
    Passed
    Beats 30% of users

    Difficulty 3/10 - got the solution quickly
"""

def setZeroes(m):

    for i in range (len(m)):
        print(m[i])

    c_to_check = []

    for i in range (len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                c_to_check.append((i,j))

    c_to_change = set()
    for coordinate in c_to_check:
        for i in range(len(m)):
            c_to_change.add((i, coordinate[1]))

        for j in range(len(m[0])):
            c_to_change.add((coordinate[0], j))

    for i in range (len(m)):
        for j in range(len(m[0])):
            if (i,j) in c_to_change:
                m[i][j] = 0

    print("")
    for i in range (len(m)):
        print(m[i])



setZeroes([[2,1,2,3],[3,4,5,2],[0,3,1,0]])