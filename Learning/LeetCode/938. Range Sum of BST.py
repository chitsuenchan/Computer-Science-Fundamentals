"""
    Wrong solution below.

    Only passed 1 test case out of 41

    Difficulty 7/10
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high, result = []):
    if root:
        rangeSumBST(root.left, low, high, result)
        rangeSumBST(root.right, low, high, result)

        if root.val <= high and root.val >= low:
            result.append(root.val)

    return sum(result)


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