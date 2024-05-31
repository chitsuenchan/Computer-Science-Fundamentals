"""
    Passes 42/65 test cases

    Came up with the solution with minimal help using knowledge from word search 1.

    Problem is that the solution isn't optimized for larger test cases and I need to implement a trie data structure which I'm unfamiliar with
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        result = []

        def dfs(row, col, pointer, visited):

            # Base case 1
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or word[pointer] != board[row][col] or (
            row, col) in visited:
                return False

            # Base case 2
            if pointer == len(word) - 1:
                return True

            # Visited
            visited.add((row, col))

            # Recursive Step
            found = dfs(row + 1, col, pointer + 1, visited) or dfs(row - 1, col, pointer + 1, visited) or dfs(row,
                                                                                                              col - 1,
                                                                                                              pointer + 1,
                                                                                                              visited) or dfs(
                row, col + 1, pointer + 1, visited)

            # Backtracking
            visited.remove((row, col))

            return found

        for word in words:
            found = False
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if dfs(row, col, 0, set()):
                        result.append(word)
                        found = True
                        break

                if found:
                    break

        return result