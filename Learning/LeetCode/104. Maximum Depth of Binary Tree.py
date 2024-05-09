
"""
    Optimal Solution
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if root is None:
            return 0

        # Recursive Step

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)


