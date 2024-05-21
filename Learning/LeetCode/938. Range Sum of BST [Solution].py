"""
    Solution below
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high):

    def dfs(node):

        if not node:
            return 0

        current_val = 0
        if low <= node.val <= high:
            current_val = node.val

        left_sum = dfs(node.left)
        right_sum = dfs(node.right)

        return current_val + left_sum + right_sum

    return dfs(root)



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(6)


print(rangeSumBST(root, 6, 10))