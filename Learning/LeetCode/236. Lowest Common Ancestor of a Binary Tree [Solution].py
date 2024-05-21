"""
    Couldn't get it without looking at solution

    Difficulty 9/10
    Don't understand recursion in a binary tree (it's not Binary search tree)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    # If either p or q matches the root's value, return the root
    if root.val == p.val or root.val == q.val:
        return root

    # Look for keys in left and right subtrees
    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    # If both nodes lie in left and right subtrees, then the root is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise, check if one subtree contains both nodes
    return left_lca if left_lca else right_lca
