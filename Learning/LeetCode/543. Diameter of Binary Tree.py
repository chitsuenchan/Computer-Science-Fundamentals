"""
    Passes 38/106 test cases

    The issue is that I have two DFS function where each searches solely on the left or the right
        There is a test case that the tree has the structure such as:
            root
            root.left
            root.left.right
        The actual answer to that should be 2 because from the root to the bottom is 2 nodes.
        However, my current method returns 1 because I don't search root.left.right

        27/May/2022

    Difficulty 9/10
        Need to keep track of a diameter at each node
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs_left(root, depth = 0):
            if not root:
                return 0

            max_depth = max(dfs_left(root.left, depth + 1), depth)
            return max_depth

        def dfs_right(root, depth = 0):
            if not root:
                return 0

            max_depth = max(dfs_right(root.right, depth + 1), depth)
            return max_depth

        print(dfs_left(root))
        print(dfs_right(root))

        path = dfs_left(root) + dfs_right(root)

        return path