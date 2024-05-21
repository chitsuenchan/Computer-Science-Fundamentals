"""
    Needed to see solution for this
    Spent maybe about 1hr on this

    Trick is to check roots on both then recursively check the left and right child nodes
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    # If both trees are empty, they are equal
    if not p and not q:
        return True
    # If one of the trees is empty, they are not equal
    if not p or not q:
        return False
    # If the values at the current nodes are not equal, they are not equal
    if p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Example usage:
# Constructing two binary trees
# Tree 1:
#     1
#    / \
#   2   3
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Tree 2:
#     1
#    / \
#   2   3
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

print("Are the two trees the same?", is_same_tree(tree1, tree2))  # Output: True
