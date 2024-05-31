"""
    Needed to check the solution.

    Couple of things to note:
        - need to modify base case 1, if the letter doesn't match we return
        - modify base case 3, if it matches the length we just need to return True and don't need to check the letters anymore because this is captured in the not earlier
        - need to incoporate a visited set so we don't go around in circles and pass into the dfs function
        - need to create a boolean combining all dfs directions using or so if one is true then it will all be true
        - need to remove the current cell from the visited set (backtracking)
        - need to call the dfs in our board loop and if it returns True then we return True as well
"""

import collections


def exist(board, word):
    for i in range(len(board)):
        print(board[i])

    rows, cols = len(board), len(board[0])

    pointer = 0

    def dfs(row, col, pointer):

        # 1. Base case - If hits boundary
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return

        # 2. Base case - if reaches end but nothing
        if word[pointer] != board[row][col]:
            return

        # 3. Base case - if it completes the word search
        if pointer == len(word) - 1 and word[pointer] == board[row][col]:
            return True

        pointer += 1

        return dfs(row + 1, col) or dfs(row - 1, col) or dfs(row, col + 1) or dfs(row, col - 1)

    dfs(1, 3, pointer)


print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "A", "E"]], "SEA"))
