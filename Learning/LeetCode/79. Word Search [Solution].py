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

    def dfs(row, col, pointer, visited):

        # 1. Base case - If hits boundary
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or word[pointer] != board[row][col]:
            return

        # 2. Base case - if it completes the word
        if pointer == len(word) - 1:
            return True

        # Adding the node as seen to prevent coming back to it in other word dfs
        visited.add((row, col))

        # Recursive step
        #   - 4 DFS calls for each direction (up,right,down,left)
        #   - DFS calls are chained with an or so if one of the DFS searches returns True all will be True
        #   - Save the boolean found inside a found variable
        found = dfs(row + 1, col, pointer + 1, visited) or dfs(row - 1, col, pointer + 1, visited) or dfs(row, col + 1, pointer + 1, visited) or dfs(row, col - 1, pointer + 1, visited)

        # Backtracking - remove our visited node so we can search this node again for future searches
        visited.remove((row, col))

        # Return the found boolean (either True or nothing)
        return found

    rows, cols = len(board), len(board[0])
    visited = set()
    pointer = 0

    for row in range(rows):
        for col in range(cols):

            # If dfs returns True then we will return True as well
            if dfs(row, col, pointer, visited):
                return True

    return False


print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "A", "E"]], "SEA"))
