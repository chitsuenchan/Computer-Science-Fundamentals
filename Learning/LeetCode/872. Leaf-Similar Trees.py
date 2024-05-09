"""
    Optimal Solution
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_leafs(node, leaf_lst):

    # Base Cases
    if node is None:
        return

    if node.left is None and node.right is None:
        leaf_lst.append(node.val)
        return leaf_lst

    # Recursive Step
    get_leafs(node.left, leaf_lst)
    get_leafs(node.right, leaf_lst)


def leafSimilar(root1, root2):

    leaf_lst_1 = []
    leaf_lst_2 = []

    get_leafs(root1, leaf_lst_1)
    get_leafs(root2, leaf_lst_2)

    return True


# Example usage:
# Constructing two binary trees
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

# Check if the leaf sequences are similar
print(leafSimilar(root1, root2))  # Output: True
